from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'db_simulador.json')
db = TinyDB(DB_PATH, storage=CachingMiddleware(JSONStorage))

# Tablas del sistema energético
tables = {
    "celulas": db.table('celulas'),
    "organulos": db.table('organulos'),
    "tejidos": db.table('tejidos'),
    "organos": db.table('organos'),
    "logs": db.table('logs'),
    "config": db.table('config'),
    "generadores": db.table('generadores'),
    "arranques": db.table('arranques'),
    "tipos": db.table('tipos'),
    "usuarios": db.table('usuarios'),
    "conexiones": db.table('conexiones'),
    "racks": db.table('racks')   # <--- ¡Añade esto!
}


# Alias rápidos
celulas_table     = tables["celulas"]
organulos_table   = tables["organulos"]
tejidos_table     = tables["tejidos"]
organos_table     = tables["organos"]
logs_table        = tables["logs"]
config_table      = tables["config"]
generadores_table = tables["generadores"]
arranques_table   = tables["arranques"]
tipos_table       = tables["tipos"]
usuarios_table    = tables["usuarios"]
conexiones_table  = tables["conexiones"]
racks_table = tables["racks"]

# Queries reutilizables
CelulaQuery      = Query()
OrganuloQuery    = Query()
TejidoQuery      = Query()
OrganoQuery      = Query()
LogQuery         = Query()
ConfigQuery      = Query()
GeneradorQuery   = Query()
ArranqueQuery    = Query()
TipoQuery        = Query()
UsuarioQuery     = Query()
ConexionQuery    = Query()
