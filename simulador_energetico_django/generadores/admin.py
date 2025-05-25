from django.contrib import admin

# Register your models here.
from .models import Generador
from .models import TipoGenerador
from .models import Arranque
from .models import Rack

admin.site.register(Generador)
admin.site.register(TipoGenerador)
admin.site.register(Arranque)
admin.site.register(Rack)
