from django import forms
from django.forms import ModelForm
from .models import *



class Simulacion_MF(ModelForm):
	class Meta:
		model = Simulacion
		fields = "__all__"


class ResultadoSimulacion_MF(ModelForm):
	class Meta:
		model = ResultadoSimulacion
		fields = "__all__"
