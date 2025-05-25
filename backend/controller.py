from db import celulas_table, organulos_table, generadores_table
from logger import log_event
from uuid import uuid4
import random
from costs_and_requirements import celula_puede_evolucionar, COSTO_CREAR_CELULA
from engine import energia_generada_por
from populate_db import poblar_celulas_canvas, dict_plantillas, instanciar_celula_desde_plantilla
from parche_realismo import (
    calcular_consumo_total,
    calcular_generacion_total,
    validar_generador_vs_consumo,
    balancear_rack,
    corregir_superposiciones,
    evolucionar_realista
)

plantilla_dict= dict_plantillas

impulsados = set()
celulas_activadas_recientemente = set()
# === FUNCIONES CRUD UNIVERSALES PARA CELULAS/ORGÁNULOS/GENS ===

def crear_celula(data):
    # Asegura mínimo 'id', 'tipo' y 'ubicacion'
    if "id" not in data: from uuid import uuid4; data["id"] = "C" + uuid4().hex[:6]
    if "tipo" not in data: data["tipo"] = "G"
    if "ubicacion" not in data: data["ubicacion"] = {"x":0, "y":0}
    if "energia_actual" not in data: data["energia_actual"] = 0.2
    if "energia_maxima" not in data: data["energia_maxima"] = 10
    if "organulos" not in data: data["organulos"] = []
    celulas_table.insert(data)

def editar_celula(id, cambios):
    celulas_table.update(cambios, lambda c: c["id"] == id)

def eliminar_celula(id):
    celulas_table.remove(lambda c: c["id"] == id)

def crear_organulo(data):
    if "id" not in data: from uuid import uuid4; data["id"] = "O" + uuid4().hex[:6]
    if "tipo" not in data: data["tipo"] = "O0"
    if "celula_asociada" not in data: data["celula_asociada"] = ""
    organulos_table.insert(data)

def editar_organulo(id, cambios):
    organulos_table.update(cambios, lambda o: o["id"] == id)

def eliminar_organulo(id):
    organulos_table.remove(lambda o: o["id"] == id)

# === CONEXIONES CRUD (AJUSTA A TU MODELO) ===
# Puedes almacenar conexiones en una tabla aparte, o como enlaces dentro de las células.
def obtener_conexiones():
    celulas = celulas_table.all()
    conexiones = []
    for cel in celulas:
        for enl in cel.get("enlaces", []):
            conexiones.append({"origen": cel["id"], "destino": enl})
    return conexiones

def crear_conexion(data):
    # data = {"origen": "C1", "destino": "C2"}
    celulas_table.update(
        lambda c: c["id"] == data["origen"],
        lambda c: c.setdefault("enlaces", []).append(data["destino"])
    )

def eliminar_conexion(cid):
    # cid formato "origen-destino"
    if "-" in cid:
        origen, destino = cid.split("-", 1)
        celulas_table.update(
            lambda c: c["id"] == origen,
            lambda c: c.update({"enlaces": [d for d in c.get("enlaces", []) if d != destino]})
        )

def cargar_inicial():
    # Llama a tu nuevo populate, no al antiguo
    from populate_db import poblar_celulas_canvas
    poblar_celulas_canvas()
    log_event("sistema", "Red energética inicial cargada", "sistema")



def evolucionar(ciclos=1):
    resultados = []
    global celulas_activadas_recientemente
    celulas_activadas_recientemente = set()

    for ciclo in range(ciclos):
        log_event("ciclo", f"== CICLO {ciclo + 1} ==", f"ciclo-{ciclo + 1}")
        celulas = celulas_table.all()
        organulos = organulos_table.all()
        generadores = generadores_table.all()  # Añade esto si tienes generadores físicos

        for cel in celulas:
            if not puede_arrancar_celula(cel):
                log_event("error", f"{cel['id']} no cumple condiciones de arranque", cel["id"])
                continue

            # 1. Cálculo realista de consumo y generación
            consumo = calcular_consumo_total(cel)  # Aquí puedes pasar acciones si lo deseas
            generacion = calcular_generacion_total(cel, organulos, generadores)

            energia_actual = cel.get("energia_actual", 0)
            energia_maxima = cel.get("energia_maxima", 10)
            nueva_energia = max(0, min(energia_actual + generacion - consumo, energia_maxima))
            if "energia_actual" not in cel:
                log_event("error", f"CELULA MAL FORMADA: {cel.get('id', '?')} sin energia_actual", cel.get("id"))

            celulas_table.update({"energia_actual": nueva_energia}, lambda c: c["id"] == cel["id"])
            log_event(
                "energia",
                f"{cel['id']} generó {generacion:.2f} kW, consumió {consumo:.2f} kW",
                cel["id"]
            )

            # 2. Validación: ¿el generador puede con la carga?
            if "generadores" in cel:
                for gid in cel["generadores"]:
                    gen = next((g for g in generadores if g["id"] == gid), None)
                    if gen:
                        ok, total = validar_generador_vs_consumo(gen, [cel])
                        if not ok:
                            log_event("sobrecarga", f"Generador {gid} no puede con el consumo de {cel['id']} ({total:.2f} > {gen['potencia_kw']*gen.get('eficiencia',0.85):.2f})", cel["id"])
                            resultados.append(f"{cel['id']} sin energía por sobrecarga de generador")
                            continue

            # 3. Activación y evolución si hay energía suficiente
            if nueva_energia >= 1:
                nueva_energia -= 1
                celulas_table.update({"energia_actual": nueva_energia}, lambda c: c["id"] == cel["id"])
                log_event("activacion", f"{cel['id']} activada", cel["id"])
                resultados.append(f"{cel['id']} activada con éxito")
                celulas_activadas_recientemente.add(cel["id"])

                # Registro histórico
                celulas_table.update(
                    lambda c: c["id"] == cel["id"],
                    lambda c: c.setdefault("historial", []).append(f"Activación ciclo {ciclo+1}: Gen {generacion:.2f} kW, Consumo {consumo:.2f} kW")
                )

                ciclos_previos = cel.get("ciclos_activada", 0) + 1
                celulas_table.update({"ciclos_activada": ciclos_previos}, lambda c: c["id"] == cel["id"])

                # Evolución automática si cumple criterios
                if ciclos_previos >= 3 and nueva_energia >= COSTO_CREAR_CELULA:
                    if celula_puede_evolucionar(cel, organulos):
                        siguiente_tipo = random.choice(["G", "A", "D", "S"])
                        plantillas = plantilla_dict
                        plantilla = plantillas[siguiente_tipo]
                        dx = random.randint(-80, 80)
                        dy = random.randint(-80, 80)
                        nueva_pos = {
                            "x": cel["ubicacion"]["x"] + dx,
                            "y": cel["ubicacion"]["y"] + dy
                        }
                        nueva_id, _ = instanciar_celula_desde_plantilla(
                            plantilla=plantilla,
                            posicion=nueva_pos,
                            madre=cel["id"],
                            sufijo_id=uuid4().hex[:4],
                            estado="activa",
                            nivel_evolucion=cel.get("nivel_evolucion", 1) + 1,
                            enlaces=[cel["id"]],
                            posibles_evoluciones=plantilla.get("posibles_evoluciones", []),
                        )
                        log_event("nacimiento", f"{nueva_id} generada por {cel['id']}", nueva_id)
                        celulas_table.update(
                            lambda c: c["id"] == cel["id"],
                            lambda c: c.setdefault("historial", []).append(f"Generó célula hija {nueva_id} en ciclo {ciclo+1}")
                        )
                        nueva_energia -= COSTO_CREAR_CELULA
                        celulas_table.update({"energia_actual": nueva_energia}, lambda c: c["id"] == cel["id"])
            else:
                log_event("fallo", f"{cel['id']} sin energía suficiente", cel["id"])
                resultados.append(f"{cel['id']} no pudo activarse")
                celulas_table.update(
                    lambda c: c["id"] == cel["id"],
                    lambda c: c.setdefault("historial", []).append(f"Fallo por falta de energía en ciclo {ciclo+1}")
                )

    return resultados

def impulsar_celula(celula_id):
    celula = celulas_table.get(lambda c: c["id"] == celula_id)
    if not celula:
        return False
    for o in organulos_table.all():
        if o["tipo"] == "O0" and o["celula_asociada"] == celula_id:
            impulsados.add(o["id"])
            log_event("impulso", f"{celula_id} recibió impulso manual", celula_id)
            celulas_table.update(
                lambda c: c["id"] == celula_id,
                lambda c: c.setdefault("historial", []).append("Impulso manual recibido")
            )
            return True
    return False

# Función utilitaria para devolver toda la red de células y organelos (por ejemplo para visualización)
def obtener_estado_red():
    celulas = celulas_table.all()
    organulos = organulos_table.all()
    return {
        "celulas": celulas,
        "organulos": organulos
    }



# -----------------------------------------
# Añadidos de funciones útiles y avanzadas
# -----------------------------------------

from populate_db import dict_plantillas  # O como lo llames

def instanciar_celula_tipo(tipo, posicion, madre=None, sufijo_id=None, estado="activa"):
    plantilla = dict_plantillas.get(tipo)
    if not plantilla:
        raise ValueError(f"Tipo de célula desconocido: {tipo}")
    celula_id, organulo_ids = instanciar_celula_desde_plantilla(
        plantilla=plantilla,
        posicion=posicion,
        madre=madre,
        sufijo_id=sufijo_id,
        estado=estado,
        nivel_evolucion=1,
    )
    log_event("instanciacion", f"Instanciada célula {celula_id} de tipo {tipo} en {posicion}", celula_id)
    return celula_id


def conectar_celulas(origen_id, destino_id):
    """
    Crea un enlace funcional entre dos células.
    """
    origen = celulas_table.get(lambda c: c["id"] == origen_id)
    destino = celulas_table.get(lambda c: c["id"] == destino_id)
    if not origen or not destino:
        return False
    enlaces = set(origen.get("enlaces", []))
    enlaces.add(destino_id)
    celulas_table.update({"enlaces": list(enlaces)}, lambda c: c["id"] == origen_id)
    log_event("enlace", f"Conectada {origen_id} -> {destino_id}", origen_id)
    return True

def obtener_historial_celula(celula_id):
    """
    Devuelve el historial de eventos de una célula.
    """
    celula = celulas_table.get(lambda c: c["id"] == celula_id)
    if celula:
        return celula.get("historial", [])
    return []

def listar_celulas_por_tipo(tipo):
    """
    Devuelve todas las células de un tipo específico.
    """
    return [c for c in celulas_table.all() if c["tipo"] == tipo]

def obtener_energia_total_red():
    """
    Calcula la energía total actual de la red.
    """
    return sum(c.get("energia_actual", 0) for c in celulas_table.all())

def reiniciar_red():
    """
    Resetea completamente la red (útil para pruebas rápidas).
    """
    celulas_table.truncate()
    organulos_table.truncate()
    log_event("reset", "Red energética completamente reiniciada", "sistema")

def clonar_celula(celula_id, nueva_posicion):
    """
    Crea un clon de una célula (nuevo id, mismos parámetros, nueva posición).
    """
    celula = celulas_table.get(lambda c: c["id"] == celula_id)
    if not celula:
        return None
    nueva_id = f"{celula_id}-CLONE-{uuid4().hex[:4]}"
    # Clona organulos
    nuevos_organulos = []
    nuevos_ids = []
    for o_id in celula.get("organulos", []):
        org = organulos_table.get(lambda o: o["id"] == o_id)
        if org:
            new_org_id = f"{nueva_id}-{org['id']}"
            new_org = org.copy()
            new_org["id"] = new_org_id
            new_org["celula_asociada"] = nueva_id
            nuevos_organulos.append(new_org)
            nuevos_ids.append(new_org_id)
    organulos_table.insert_multiple(nuevos_organulos)
    # Crea nueva célula
    new_cel = celula.copy()
    new_cel["id"] = nueva_id
    new_cel["ubicacion"] = nueva_posicion
    new_cel["organulos"] = nuevos_ids
    new_cel["historial"] = [f"Clon creada desde {celula_id}"]
    celulas_table.insert(new_cel)
    log_event("clonacion", f"Clonada {celula_id} como {nueva_id} en {nueva_posicion}", nueva_id)
    return nueva_id

def estado_celula(celula_id):
    """
    Devuelve el estado completo de una célula y sus organelos.
    """
    cel = celulas_table.get(lambda c: c["id"] == celula_id)
    if not cel:
        return None
    orgs = [o for o in organulos_table.all() if o["celula_asociada"] == celula_id]
    return {"celula": cel, "organulos": orgs}

# --------------------------
# Utils para frontend/canvas
# --------------------------

def info_para_canvas():
    """
    Devuelve toda la red lista para pintar en canvas: células, conexiones y atributos visuales.
    """
    celulas = celulas_table.all()
    organulos = organulos_table.all()
    nodos = []
    enlaces = []
    for c in celulas:
        nodos.append({
            "id": c["id"],
            "tipo": c["tipo"],
            "x": c["ubicacion"]["x"],
            "y": c["ubicacion"]["y"],
            "estado": c["estado"],
            "energia": c.get("energia_actual", 0),
            "organulos": c.get("organulos", [])
        })
        for e in c.get("enlaces", []):
            enlaces.append({
                "origen": c["id"],
                "destino": e
            })
    return {"nodos": nodos, "enlaces": enlaces, "organulos": organulos}


def desconectar_celulas(origen, destino):
    # Elimina enlace bidireccional
    cel = celulas_table.get(lambda c: c["id"] == origen)
    if not cel:
        return False
    enlaces = set(cel.get("enlaces", []))
    if destino in enlaces:
        enlaces.remove(destino)
        celulas_table.update({"enlaces": list(enlaces)}, lambda c: c["id"] == origen)
    # Repite para la otra célula (si simétrico)
    cel2 = celulas_table.get(lambda c: c["id"] == destino)
    if cel2:
        enlaces2 = set(cel2.get("enlaces", []))
        if origen in enlaces2:
            enlaces2.remove(origen)
            celulas_table.update({"enlaces": list(enlaces2)}, lambda c: c["id"] == destino)
    return True


import math
from populate_db import todas_plantillas, instanciar_celula_desde_plantilla

def randomizar_organismo_param(params):
    # Limpiar la red primero
    from db import celulas_table, organulos_table
    celulas_table.truncate()
    organulos_table.truncate()
    # Parámetros de entrada
    num_celulas = int(params.get("numCelulas", 10))
    pct_germinadoras = int(params.get("pctGerminadoras", 30))
    pct_amplificadoras = int(params.get("pctAmplificadoras", 20))
    pct_distribuidoras = int(params.get("pctDistribuidoras", 20))
    pct_estabilizadoras = int(params.get("pctEstabilizadoras", 20))
    energia_min = float(params.get("energiaMin", 0.2))
    energia_max = float(params.get("energiaMax", 2.0))
    num_conexiones = int(params.get("numConexiones", 2))

    tipos = []
    tipos += ["G"] * math.ceil(num_celulas * pct_germinadoras / 100)
    tipos += ["A"] * math.ceil(num_celulas * pct_amplificadoras / 100)
    tipos += ["D"] * math.ceil(num_celulas * pct_distribuidoras / 100)
    tipos += ["S"] * (num_celulas - len(tipos))  # Rellena el resto con estabilizadoras si sobra

    random.shuffle(tipos)

    ids_celulas = []
    posiciones = []
    ancho, alto = 1000, 800
    for i, t in enumerate(tipos):
        plantilla = next((p for p in todas_plantillas if p["tipo"] == t), todas_plantillas[0])
        x = random.randint(80, ancho - 80)
        y = random.randint(80, alto - 80)
        energia = round(random.uniform(energia_min, energia_max), 2)
        cel_id, _ = instanciar_celula_desde_plantilla(
            plantilla=plantilla,
            posicion={"x": x, "y": y},
            madre=None,
            sufijo_id=str(i+1),
            estado="activa",
            nivel_evolucion=1,
            enlaces=[],
            posibles_evoluciones=plantilla.get("posibles_evoluciones", []),
        )
        # Sobrescribe la energía si hace falta
        celulas_table.update({"energia_actual": energia}, lambda c: c["id"] == cel_id)
        ids_celulas.append(cel_id)
        posiciones.append({"x": x, "y": y})

    # Conectar las células aleatoriamente según num_conexiones
    for idx, cid in enumerate(ids_celulas):
        enlaces = set()
        while len(enlaces) < num_conexiones:
            otro = random.choice(ids_celulas)
            if otro != cid:
                enlaces.add(otro)
        celulas_table.update({"enlaces": list(enlaces)}, lambda c: c["id"] == cid)

    log_event("random", f"Organismo random creado con {num_celulas} células.")
    return {"n_celulas": num_celulas, "tipos": tipos, "ids": ids_celulas}


# En controller.py




# === FUNCIONES BÁSICAS PARA CRUD ===

def crear_generador(data): generadores_table.insert(data)
def editar_generador(id, cambios): generadores_table.update(cambios, lambda g: g["id"]==id)
def eliminar_generador(id): generadores_table.remove(lambda g: g["id"]==id)
def editar_conexion(origen_id, destino_id, nueva_info):
    """
    Edita la información de la conexión entre dos células/orgánulos.
    Si usas dicts, puedes almacenar info extra (peso, tipo, etc.).
    """
    celula = celulas_table.get(lambda c: c["id"] == origen_id)
    if not celula:
        return False
    enlaces = celula.get("enlaces", [])
    for enlace in enlaces:
        # Si guardas solo el id, este bloque cambia.
        if (isinstance(enlace, dict) and enlace.get("destino") == destino_id):
            enlace.update(nueva_info)
            celulas_table.update({"enlaces": enlaces}, lambda c: c["id"] == origen_id)
            log_event("edicion", f"Conexión {origen_id}->{destino_id} editada: {nueva_info}", origen_id)
            return True
    return False
from parche_realismo import validar_generador_vs_consumo, balancear_rack

def puede_crear_celula(nueva_celula, generadores, celulas_existentes):
    """
    Valida si la red soporta una nueva célula sin sobrecargar generadores o racks.
    """
    # 1. Si la célula va asociada a generador físico concreto
    if "generadores" in nueva_celula:
        for gid in nueva_celula["generadores"]:
            gen = next((g for g in generadores if g["id"] == gid), None)
            if gen:
                # Obtén todas las células asociadas a este generador
                cels_asociadas = [c for c in celulas_existentes if "generadores" in c and gid in c["generadores"]]
                cels_asociadas.append(nueva_celula)
                ok, total = validar_generador_vs_consumo(gen, cels_asociadas)
                if not ok:
                    return False, f"Generador {gid} sobrecargado ({total:.2f} kW > {gen['potencia_kw']*gen.get('eficiencia',0.85):.2f})"
    # 2. Si modelo de racks: puedes ampliar aquí
    # 3. O validación global si quieres impedir cualquier expansión que supere la potencia total de la red
    return True, "OK"
def crear_celula_validada(data):
    generadores = generadores_table.all()
    celulas_existentes = celulas_table.all()
    ok, msg = puede_crear_celula(data, generadores, celulas_existentes)
    if not ok:
        log_event("expansion_bloqueada", msg, data.get("id","?"))
        raise Exception(f"Creación de célula bloqueada: {msg}")
    crear_celula(data)  # Si pasa el filtro, crea la célula
def puede_expandir_rack(nuevo_rack, racks, generadores, celulas):
    """
    Valida si el rack tendrá suficiente potencia para todas las células asociadas.
    """
    gens = [g for g in generadores if g["id"] in nuevo_rack["generadores"]]
    cels = [c for c in celulas if c["id"] in nuevo_rack["celulas"]]
    ok, factor = balancear_rack(gens, cels)
    if not ok:
        return False, f"Rack {nuevo_rack['id']} sobrecargado (factor balanceo={factor:.2f})"
    return True, "OK"

def puede_arrancar_celula(celula):
    # Ejemplo: requiere al menos un orgánulo solar (O11) o manual (O0)
    organulos = celula.get("organulos", [])
    if not organulos:
        return False
    # Si son IDs, deberías consultar en organulos_table, si ya son dict, mira el tipo:
    for o in organulos:
        tipo = o["tipo"] if isinstance(o, dict) else organulos_table.get(lambda x: x["id"] == o)["tipo"]
        if tipo in ("O0", "O11"):
            return True
    return False



