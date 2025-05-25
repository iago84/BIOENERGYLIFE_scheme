from django import forms
from django.forms import ModelForm
from .models import *



class Organulo_MF(ModelForm):
	class Meta:
		model = Organulo
		fields = "__all__"


class TipoOrganulo_MF(ModelForm):
	class Meta:
		model = TipoOrganulo
		fields = "__all__"


class Secuenciador_MF(ModelForm):
	class Meta:
		model = Secuenciador
		fields = "__all__"


class DispositivoControl_MF(ModelForm):
	class Meta:
		model = DispositivoControl
		fields = "__all__"
