from django import forms
from django.forms import ModelForm
from .models import *



class Celula_MF(ModelForm):
	class Meta:
		model = Celula
		fields = "__all__"


class EstadoCelula_MF(ModelForm):
	class Meta:
		model = EstadoCelula
		fields = "__all__"


class EvolucionCelula_MF(ModelForm):
	class Meta:
		model = EvolucionCelula
		fields = "__all__"


class UbicacionCelula_MF(ModelForm):
	class Meta:
		model = UbicacionCelula
		fields = "__all__"
