from django.contrib import admin

# Register your models here.
from .models import Simulacion
from .models import ResultadoSimulacion

admin.site.register(Simulacion)
admin.site.register(ResultadoSimulacion)
