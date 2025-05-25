from rest_framework import serializers
from .models import *


class CelulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celula
        fields = "__all__"

class EstadoCelulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCelula
        fields = "__all__"

class EvolucionCelulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvolucionCelula
        fields = "__all__"

class UbicacionCelulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UbicacionCelula
        fields = "__all__"
