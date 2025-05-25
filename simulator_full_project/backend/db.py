from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware
import os

# Ruta del archivo de base de datos
DB_PATH = os.path.join(os.path.dirname(__file__), 'db_simulador.json')

# Inicialización con caché
db = TinyDB(DB_PATH, storage=CachingMiddleware(JSONStorage))

# Tablas del sistema energético
tables = {
    "celulas": db.table('celulas'),
    "organulos": db.table('organulos'),
    "tejidos": db.table('tejidos'),
    "organos": db.table('organos'),
    "logs": db.table('logs'),
    "config": db.table('config'),
    "generadores": db.table('generadores')
}

# Alias rápidos
celulas_table = tables["celulas"]
organulos_table = tables["organulos"]
tejidos_table = tables["tejidos"]
organos_table = tables["organos"]
logs_table = tables["logs"]
config_table = tables["config"]
generadores_table = tables["generadores"]

# Queries reutilizables
CelulaQuery = Query()
OrganuloQuery = Query()
TejidoQuery = Query()
OrganoQuery = Query()
LogQuery = Query()
ConfigQuery = Query()
GeneradorQuery = Query()
