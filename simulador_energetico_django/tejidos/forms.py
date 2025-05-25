from django import forms
from django.forms import ModelForm
from .models import *



class Tejido_MF(ModelForm):
	class Meta:
		model = Tejido
		fields = "__all__"


class TipoTejido_MF(ModelForm):
	class Meta:
		model = TipoTejido
		fields = "__all__"
