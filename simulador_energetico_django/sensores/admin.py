from django.contrib import admin

# Register your models here.
from .models import Sensor
from .models import Medidor
from .models import TipoSensor

admin.site.register(Sensor)
admin.site.register(Medidor)
admin.site.register(TipoSensor)
