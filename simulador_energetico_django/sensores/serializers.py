from rest_framework import serializers
from .models import *


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = "__all__"

class MedidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medidor
        fields = "__all__"

class TipoSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSensor
        fields = "__all__"
