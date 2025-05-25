from rest_framework.generics import *
from rest_framework import permissions
from .models import *
from .serializers import *

class SimulacionListAPIView(ListAPIView):
    queryset = Simulacion.objects.all()
    serializer_class = SimulacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class SimulacionCreateAPIView(CreateAPIView):
    queryset = Simulacion.objects.all()
    serializer_class = SimulacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class SimulacionRetrieveAPIView(RetrieveAPIView):
    queryset = Simulacion.objects.all()
    serializer_class = SimulacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class SimulacionUpdateAPIView(UpdateAPIView):
    queryset = Simulacion.objects.all()
    serializer_class = SimulacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class SimulacionDestroyAPIView(DestroyAPIView):
    queryset = Simulacion.objects.all()
    serializer_class = SimulacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class ResultadoSimulacionListAPIView(ListAPIView):
    queryset = ResultadoSimulacion.objects.all()
    serializer_class = ResultadoSimulacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ResultadoSimulacionCreateAPIView(CreateAPIView):
    queryset = ResultadoSimulacion.objects.all()
    serializer_class = ResultadoSimulacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ResultadoSimulacionRetrieveAPIView(RetrieveAPIView):
    queryset = ResultadoSimulacion.objects.all()
    serializer_class = ResultadoSimulacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ResultadoSimulacionUpdateAPIView(UpdateAPIView):
    queryset = ResultadoSimulacion.objects.all()
    serializer_class = ResultadoSimulacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class ResultadoSimulacionDestroyAPIView(DestroyAPIView):
    queryset = ResultadoSimulacion.objects.all()
    serializer_class = ResultadoSimulacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

