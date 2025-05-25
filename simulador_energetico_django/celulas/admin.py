from django.contrib import admin

# Register your models here.
from .models import Celula
from .models import EstadoCelula
from .models import EvolucionCelula
from .models import UbicacionCelula

admin.site.register(Celula)
admin.site.register(EstadoCelula)
admin.site.register(EvolucionCelula)
admin.site.register(UbicacionCelula)
