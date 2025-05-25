from django.contrib import admin

# Register your models here.
from .models import Tejido
from .models import TipoTejido

admin.site.register(Tejido)
admin.site.register(TipoTejido)
