from rest_framework import serializers
from .models import *


class CargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carga
        fields = "__all__"

class TipoCargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCarga
        fields = "__all__"
