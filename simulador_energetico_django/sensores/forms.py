from django import forms
from django.forms import ModelForm
from .models import *



class Sensor_MF(ModelForm):
	class Meta:
		model = Sensor
		fields = "__all__"


class Medidor_MF(ModelForm):
	class Meta:
		model = Medidor
		fields = "__all__"


class TipoSensor_MF(ModelForm):
	class Meta:
		model = TipoSensor
		fields = "__all__"
