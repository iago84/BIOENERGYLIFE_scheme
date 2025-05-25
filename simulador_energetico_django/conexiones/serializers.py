from rest_framework import serializers
from .models import *


class ConexionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conexion
        fields = "__all__"

class TipoConexionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoConexion
        fields = "__all__"
