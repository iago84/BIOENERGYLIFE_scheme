from rest_framework import serializers
from .models import *


class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = "__all__"

class ParametroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametro
        fields = "__all__"

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"
