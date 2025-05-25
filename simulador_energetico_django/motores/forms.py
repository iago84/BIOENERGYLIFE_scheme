from django import forms
from django.forms import ModelForm
from .models import *



class Motor_MF(ModelForm):
	class Meta:
		model = Motor
		fields = "__all__"


class TipoMotor_MF(ModelForm):
	class Meta:
		model = TipoMotor
		fields = "__all__"
