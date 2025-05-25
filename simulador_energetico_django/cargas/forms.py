from django import forms
from django.forms import ModelForm
from .models import *



class Carga_MF(ModelForm):
	class Meta:
		model = Carga
		fields = "__all__"


class TipoCarga_MF(ModelForm):
	class Meta:
		model = TipoCarga
		fields = "__all__"
