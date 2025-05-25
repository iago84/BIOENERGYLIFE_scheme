from rest_framework.generics import *
from rest_framework import permissions
from .models import *
from .serializers import *

class SensorListAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class SensorCreateAPIView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class SensorRetrieveAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class SensorUpdateAPIView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class SensorDestroyAPIView(DestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class MedidorListAPIView(ListAPIView):
    queryset = Medidor.objects.all()
    serializer_class = MedidorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class MedidorCreateAPIView(CreateAPIView):
    queryset = Medidor.objects.all()
    serializer_class = MedidorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class MedidorRetrieveAPIView(RetrieveAPIView):
    queryset = Medidor.objects.all()
    serializer_class = MedidorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class MedidorUpdateAPIView(UpdateAPIView):
    queryset = Medidor.objects.all()
    serializer_class = MedidorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class MedidorDestroyAPIView(DestroyAPIView):
    queryset = Medidor.objects.all()
    serializer_class = MedidorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class TipoSensorListAPIView(ListAPIView):
    queryset = TipoSensor.objects.all()
    serializer_class = TipoSensorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoSensorCreateAPIView(CreateAPIView):
    queryset = TipoSensor.objects.all()
    serializer_class = TipoSensorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class TipoSensorRetrieveAPIView(RetrieveAPIView):
    queryset = TipoSensor.objects.all()
    serializer_class = TipoSensorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoSensorUpdateAPIView(UpdateAPIView):
    queryset = TipoSensor.objects.all()
    serializer_class = TipoSensorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class TipoSensorDestroyAPIView(DestroyAPIView):
    queryset = TipoSensor.objects.all()
    serializer_class = TipoSensorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

