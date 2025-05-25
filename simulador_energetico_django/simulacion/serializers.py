from rest_framework import serializers
from .models import *


class SimulacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simulacion
        fields = "__all__"

class ResultadoSimulacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoSimulacion
        fields = "__all__"
