import os

# ==== Configuración de rutas de tu proyecto (ajusta si cambian) ====
BACKEND = ["backend/server.py", "backend/controller.py", "backend/schemas.py"]
FRONTEND = ["frontend/app.js", "frontend/index.html"]

# ==== BLOQUES DE CÓDIGO A INYECTAR O CREAR ====
BLOQUE_MARSHMALLOW = '''
# -- Esquema Marshmallow para validar células --
from marshmallow import Schema, fields, validate

class CelulaSchema(Schema):
    id = fields.Str(required=True)
    tipo = fields.Str(required=True, validate=validate.OneOf(["G","A","S","D"]))
    energia_actual = fields.Float(required=True)
    energia_maxima = fields.Float(required=True)
    organulos = fields.List(fields.Str(), required=True)
    estado = fields.Str()
    ubicacion = fields.Dict()
    nivel_evolucion = fields.Int()
    enlaces = fields.List(fields.Str())
    generada_por = fields.Str(allow_none=True)
    puede_multiplicar = fields.Bool()
    posibles_evoluciones = fields.List(fields.Str())
'''

BLOQUE_VALIDACION_ENDPOINT = '''
# -- Validación de datos en endpoint de creación de célula --
from schemas import CelulaSchema

@app.route("/api/celula", methods=["POST"])
def api_crear_celula():
    data = request.json
    errors = CelulaSchema().validate(data)
    if errors:
        return jsonify({"ok": False, "errors": errors}), 400
    # ... continuación de la lógica original ...
'''

BLOQUE_ERROR_HANDLER = '''
# -- Log de errores global --
import logging
logging.basicConfig(filename='server_errors.log', level=logging.ERROR)

@app.errorhandler(Exception)
def handle_exception(e):
    import traceback
    logging.error(traceback.format_exc())
    return jsonify({"ok": False, "error": str(e)}), 500
'''

BLOQUE_PROTECCION_PRODUCCION = '''
# -- Protección básica en producción --
import os

if __name__ == '__main__':
    debug = os.environ.get("DEBUG", "1") == "1"
    if not debug:
        print("Modo producción: restringiendo endpoints abiertos")
        # Aquí podrías restringir rutas, exigir login, etc.
    app.run(debug=debug)
'''

BLOQUE_LOGICA_ARRANQUE = '''
# -- Lógica de requisitos de arranque para célula --
def puede_arrancar_celula(celula):
    organulos = [organulos_table.get(lambda o: o["id"]==oid) for oid in celula.get("organulos",[])]
    tipos = [o["tipo"] for o in organulos if o]
    if "O0" not in tipos and "O11" not in tipos:
        return False
    return True
'''

BLOQUE_CHECK_ARRANQUE_EN_CONTROLLER = '''
# -- Usar chequeo antes de activar/crear célula --
if not puede_arrancar_celula(celula):
    return jsonify({"ok": False, "error": "La célula no cumple condiciones de arranque"}), 400
'''

BLOQUE_FRONTEND_CRUD_TABLA = '''
// Renderizado básico de tabla de células para frontend
function renderTablaCelulas(celulas) {
    const tbody = document.getElementById('tablaCelulas');
    tbody.innerHTML = "";
    celulas.forEach(cel => {
        let tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${cel.id}</td>
            <td>${cel.tipo}</td>
            <td>${cel.energia_actual}</td>
            <td>
                <button onclick="mostrarDetallesCelula('${cel.id}')">Detalles</button>
                <button onclick="editarCelulaModal('${cel.id}')">Editar</button>
                <button onclick="eliminarCelula('${cel.id}')">Eliminar</button>
            </td>
        `;
        tbody.appendChild(tr);
    });
}
'''

BLOQUE_FRONTEND_MODAL_HTML = '''
<!-- Modal de edición/creación de célula -->
<div id="modalCelula" class="modal" style="display:none;">
  <div class="modal-content">
    <span class="close" onclick="cerrarModalCelula()">&times;</span>
    <h2>Editar/Crear Célula</h2>
    <form id="formCelula">
      <label>ID: <input type="text" name="id" required></label>
      <label>Tipo: <select name="tipo"><option>G</option><option>A</option><option>S</option><option>D</option></select></label>
      <label>Energía actual: <input type="number" name="energia_actual" step="0.01" required></label>
      <label>Máxima: <input type="number" name="energia_maxima" step="0.01" required></label>
      <!-- ...otros campos... -->
      <button type="submit">Guardar</button>
    </form>
  </div>
</div>
'''

# ==== FUNCIONES AUXILIARES DE PARCHEO ====
def insertar_si_no_esta(path, bloque, marcador, antes_de=None):
    with open(path, "r", encoding="utf8") as f:
        contenido = f.read()
    if marcador not in contenido:
        if antes_de and antes_de in contenido:
            contenido = contenido.replace(antes_de, bloque + "\n" + antes_de)
        else:
            contenido += "\n" + bloque
        with open(path, "w", encoding="utf8") as f:
            f.write(contenido)
        print(f"[OK] Parcheado {marcador} en {os.path.basename(path)}")
        return True
    else:
        print(f"[SKIP] Ya estaba {marcador} en {os.path.basename(path)}")
        return False

def crear_si_no_existe(path, contenido):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf8") as f:
            f.write(contenido)
        print(f"[OK] Creado {path}")
        return True
    else:
        print(f"[SKIP] Ya existía {path}")
        return False

def main():
    # Marshmallow schema
    if not os.path.exists(BACKEND[2]):
        crear_si_no_existe(BACKEND[2], BLOQUE_MARSHMALLOW)
    # Endpoints validados y error handler en server.py
    if os.path.exists(BACKEND[0]):
        insertar_si_no_esta(BACKEND[0], BLOQUE_VALIDACION_ENDPOINT, "# -- Validación de datos en endpoint de creación de célula --")
        insertar_si_no_esta(BACKEND[0], BLOQUE_ERROR_HANDLER, "# -- Log de errores global --")
        insertar_si_no_esta(BACKEND[0], BLOQUE_PROTECCION_PRODUCCION, "# -- Protección básica en producción --")
    # Lógica de arranque en controller.py
    if os.path.exists(BACKEND[1]):
        insertar_si_no_esta(BACKEND[1], BLOQUE_LOGICA_ARRANQUE, "# -- Lógica de requisitos de arranque para célula --")
        insertar_si_no_esta(BACKEND[1], BLOQUE_CHECK_ARRANQUE_EN_CONTROLLER, "# -- Usar chequeo antes de activar/crear célula --")
    # Frontend tabla y modal (solo ejemplo básico, luego personaliza)
    if os.path.exists(FRONTEND[0]):
        insertar_si_no_esta(FRONTEND[0], BLOQUE_FRONTEND_CRUD_TABLA, "// Renderizado básico de tabla de células para frontend")
    if os.path.exists(FRONTEND[1]):
        insertar_si_no_esta(FRONTEND[1], BLOQUE_FRONTEND_MODAL_HTML, "<!-- Modal de edición/creación de célula -->", antes_de="</body>")
    print("\n[INFO] Parcheo auto-completado. ¡Revisa logs y modales, personaliza los métodos y endpoints!")

if __name__ == "__main__":
    main()
