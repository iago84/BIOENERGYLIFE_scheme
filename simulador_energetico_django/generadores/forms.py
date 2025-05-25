from django import forms
from django.forms import ModelForm
from .models import *



class Generador_MF(ModelForm):
	class Meta:
		model = Generador
		fields = "__all__"


class TipoGenerador_MF(ModelForm):
	class Meta:
		model = TipoGenerador
		fields = "__all__"


class Arranque_MF(ModelForm):
	class Meta:
		model = Arranque
		fields = "__all__"


class Rack_MF(ModelForm):
	class Meta:
		model = Rack
		fields = "__all__"
