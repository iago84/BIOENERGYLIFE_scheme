from django import forms
from django.forms import ModelForm
from .models import *



class Conexion_MF(ModelForm):
	class Meta:
		model = Conexion
		fields = "__all__"


class TipoConexion_MF(ModelForm):
	class Meta:
		model = TipoConexion
		fields = "__all__"
