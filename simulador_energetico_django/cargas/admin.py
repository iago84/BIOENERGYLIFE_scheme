from django.contrib import admin

# Register your models here.
from .models import Carga
from .models import TipoCarga

admin.site.register(Carga)
admin.site.register(TipoCarga)
