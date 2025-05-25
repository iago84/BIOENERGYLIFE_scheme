from rest_framework import serializers
from .models import *


class GeneradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generador
        fields = "__all__"

class TipoGeneradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoGenerador
        fields = "__all__"

class ArranqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arranque
        fields = "__all__"

class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rack
        fields = "__all__"
