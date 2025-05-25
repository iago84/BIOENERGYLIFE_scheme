from django.contrib import admin

# Register your models here.
from .models import ReservaEnergetica
from .models import TipoReserva

admin.site.register(ReservaEnergetica)
admin.site.register(TipoReserva)
