from django.contrib import admin

# Register your models here.
from .models import Organulo
from .models import TipoOrganulo
from .models import Secuenciador
from .models import DispositivoControl

admin.site.register(Organulo)
admin.site.register(TipoOrganulo)
admin.site.register(Secuenciador)
admin.site.register(DispositivoControl)
