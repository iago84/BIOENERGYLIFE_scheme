from django.contrib import admin

# Register your models here.
from .models import Conexion
from .models import TipoConexion

admin.site.register(Conexion)
admin.site.register(TipoConexion)
