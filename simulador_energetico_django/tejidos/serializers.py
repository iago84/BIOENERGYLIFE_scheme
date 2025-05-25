from rest_framework import serializers
from .models import *


class TejidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tejido
        fields = "__all__"

class TipoTejidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTejido
        fields = "__all__"
