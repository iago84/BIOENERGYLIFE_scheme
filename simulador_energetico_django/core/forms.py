from django import forms
from django.forms import ModelForm
from .models import *



class Configuracion_MF(ModelForm):
	class Meta:
		model = Configuracion
		fields = "__all__"


class Parametro_MF(ModelForm):
	class Meta:
		model = Parametro
		fields = "__all__"


class Log_MF(ModelForm):
	class Meta:
		model = Log
		fields = "__all__"
