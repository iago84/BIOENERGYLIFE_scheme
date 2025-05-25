from rest_framework.generics import *
from rest_framework import permissions
from .models import *
from .serializers import *

class MotorListAPIView(ListAPIView):
    queryset = Motor.objects.all()
    serializer_class = MotorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class MotorCreateAPIView(CreateAPIView):
    queryset = Motor.objects.all()
    serializer_class = MotorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class MotorRetrieveAPIView(RetrieveAPIView):
    queryset = Motor.objects.all()
    serializer_class = MotorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class MotorUpdateAPIView(UpdateAPIView):
    queryset = Motor.objects.all()
    serializer_class = MotorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class MotorDestroyAPIView(DestroyAPIView):
    queryset = Motor.objects.all()
    serializer_class = MotorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class TipoMotorListAPIView(ListAPIView):
    queryset = TipoMotor.objects.all()
    serializer_class = TipoMotorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoMotorCreateAPIView(CreateAPIView):
    queryset = TipoMotor.objects.all()
    serializer_class = TipoMotorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class TipoMotorRetrieveAPIView(RetrieveAPIView):
    queryset = TipoMotor.objects.all()
    serializer_class = TipoMotorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoMotorUpdateAPIView(UpdateAPIView):
    queryset = TipoMotor.objects.all()
    serializer_class = TipoMotorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class TipoMotorDestroyAPIView(DestroyAPIView):
    queryset = TipoMotor.objects.all()
    serializer_class = TipoMotorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

