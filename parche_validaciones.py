# parche_validaciones.py

from parche_realismo import validar_generador_vs_consumo, balancear_rack

def puede_crear_celula(nueva_celula, generadores, celulas_existentes, modo_balanceo=False):
    """
    Valida si se puede crear una nueva célula sin sobrecargar ningún generador.
    Si modo_balanceo=True, ajusta el consumo de todas proporcionalmente si es necesario.
    """
    # Si la célula va asociada a generador físico concreto
    if "generadores" in nueva_celula:
        for gid in nueva_celula["generadores"]:
            gen = next((g for g in generadores if g["id"] == gid), None)
            if gen:
                cels_asociadas = [c for c in celulas_existentes if "generadores" in c and gid in c["generadores"]]
                cels_asociadas.append(nueva_celula)
                ok, total = validar_generador_vs_consumo(gen, cels_asociadas)
                if not ok:
                    if modo_balanceo:
                        # Balanceo: reduce consumo a todas para no sobrecargar
                        factor = (gen["potencia_kw"] * gen.get("eficiencia",0.85)) / total
                        for c in cels_asociadas:
                            c["consumo_kw"] = c.get("consumo_kw", 0) * factor
                        return True, f"Se aplicó balanceo automático (factor={factor:.2f})"
                    else:
                        return False, f"Generador {gid} sobrecargado ({total:.2f} kW > {gen['potencia_kw']*gen.get('eficiencia',0.85):.2f})"
    # Puedes agregar aquí validación global, si lo deseas.
    return True, "OK"


def crear_celula_validada(data, generadores, celulas_existentes, modo_balanceo=False):
    ok, msg = puede_crear_celula(data, generadores, celulas_existentes, modo_balanceo=modo_balanceo)
    if not ok:
        raise Exception(f"Creación de célula bloqueada: {msg}")
    return True, msg  # Solo crearás la célula en tu tabla si pasa el filtro.


def puede_expandir_rack(nuevo_rack, generadores, celulas, modo_balanceo=False):
    """
    Valida si el rack puede soportar su carga.
    Si modo_balanceo=True, aplica balanceo automático si es necesario.
    """
    gens = [g for g in generadores if g["id"] in nuevo_rack["generadores"]]
    cels = [c for c in celulas if c["id"] in nuevo_rack["celulas"]]
    ok, factor = balancear_rack(gens, cels)
    if not ok:
        if modo_balanceo:
            # Reducir consumo de todas para entrar en potencia
            for c in cels:
                c["consumo_kw"] = c.get("consumo_kw", 0) * factor
            return True, f"Rack balanceado automáticamente (factor={factor:.2f})"
        else:
            return False, f"Rack {nuevo_rack['id']} sobrecargado (factor balanceo={factor:.2f})"
    return True, "OK"


def expandir_rack_validado(nuevo_rack, generadores, celulas, modo_balanceo=False):
    ok, msg = puede_expandir_rack(nuevo_rack, generadores, celulas, modo_balanceo=modo_balanceo)
    if not ok:
        raise Exception(f"Expansión de rack bloqueada: {msg}")
    return True, msg  # Solo guardas el rack si pasa el filtro.

# Opción extra: validación global de red (toda la potencia vs todo el consumo)
def validar_red_global(generadores, celulas, modo_balanceo=False):
    total_pot = sum(g["potencia_kw"] * g.get("eficiencia", 0.85) for g in generadores)
    total_cons = sum(c.get("consumo_kw", 0) for c in celulas)
    if total_cons > total_pot:
        if modo_balanceo:
            factor = total_pot / total_cons
            for c in celulas:
                c["consumo_kw"] = c.get("consumo_kw", 0) * factor
            return True, f"Balanceo automático aplicado a toda la red (factor={factor:.2f})"
        else:
            return False, f"Red sobrecargada: consumo {total_cons:.2f} > potencia {total_pot:.2f}"
    return True, "OK"
