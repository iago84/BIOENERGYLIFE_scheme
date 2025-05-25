from django import forms
from django.forms import ModelForm
from .models import *



class ReservaEnergetica_MF(ModelForm):
	class Meta:
		model = ReservaEnergetica
		fields = "__all__"


class TipoReserva_MF(ModelForm):
	class Meta:
		model = TipoReserva
		fields = "__all__"
