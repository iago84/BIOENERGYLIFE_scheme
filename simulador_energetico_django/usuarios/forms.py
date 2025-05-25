from django import forms
from django.forms import ModelForm
from .models import *



class Usuario_MF(ModelForm):
	class Meta:
		model = Usuario
		fields = "__all__"


class PerfilUsuario_MF(ModelForm):
	class Meta:
		model = PerfilUsuario
		fields = "__all__"
