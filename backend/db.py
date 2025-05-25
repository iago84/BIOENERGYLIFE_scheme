from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'db_simulador.json')
db = TinyDB(DB_PATH, storage=CachingMiddleware(JSONStorage))

# Tablas optimizadas del sistema energético
tables = {
    "celulas": db.table('celulas'),
    "organulos": db.table('organulos'),
    "tejidos": db.table('tejidos'),
    "organos": db.table('organos'),
    "logs": db.table('logs'),
    "config": db.table('config'),
    "generadores": db.table('generadores'),
    "arranques": db.table('arranques'),      # Nueva tabla para métodos de arranque (opcional, si los quieres desacoplar)
    "tipos": db.table('tipos'),              # Para tipos y familias extendidas
    "usuarios": db.table('usuarios'),        # Futuro: para control multiusuario/editor
}

# Alias rápidos
celulas_table = tables["celulas"]
organulos_table = tables["organulos"]
tejidos_table = tables["tejidos"]
organos_table = tables["organos"]
logs_table = tables["logs"]
config_table = tables["config"]
generadores_table = tables["generadores"]
arranques_table = tables["arranques"]
tipos_table = tables["tipos"]
usuarios_table = tables["usuarios"]

# Queries reutilizables
CelulaQuery = Query()
OrganuloQuery = Query()
TejidoQuery = Query()
OrganoQuery = Query()
LogQuery = Query()
ConfigQuery = Query()
GeneradorQuery = Query()
ArranqueQuery = Query()
TipoQuery = Query()
UsuarioQuery = Query()
