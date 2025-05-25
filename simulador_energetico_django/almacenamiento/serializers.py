from rest_framework import serializers
from .models import *


class ReservaEnergeticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaEnergetica
        fields = "__all__"

class TipoReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoReserva
        fields = "__all__"
