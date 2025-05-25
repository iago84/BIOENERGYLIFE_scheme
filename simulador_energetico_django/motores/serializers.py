from rest_framework import serializers
from .models import *


class MotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motor
        fields = "__all__"

class TipoMotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMotor
        fields = "__all__"
