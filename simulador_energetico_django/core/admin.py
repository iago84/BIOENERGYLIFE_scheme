from django.contrib import admin

# Register your models here.
from .models import Configuracion
from .models import Parametro
from .models import Log

admin.site.register(Configuracion)
admin.site.register(Parametro)
admin.site.register(Log)
