from rest_framework import serializers
from .models import *


class OrganuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organulo
        fields = "__all__"

class TipoOrganuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOrganulo
        fields = "__all__"

class SecuenciadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secuenciador
        fields = "__all__"

class DispositivoControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispositivoControl
        fields = "__all__"
