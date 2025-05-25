from django.contrib import admin

# Register your models here.
from .models import Motor
from .models import TipoMotor

admin.site.register(Motor)
admin.site.register(TipoMotor)
