from rest_framework.generics import *
from rest_framework import permissions
from .models import *
from .serializers import *

class CelulaListAPIView(ListAPIView):
    queryset = Celula.objects.all()
    serializer_class = CelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CelulaCreateAPIView(CreateAPIView):
    queryset = Celula.objects.all()
    serializer_class = CelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class CelulaRetrieveAPIView(RetrieveAPIView):
    queryset = Celula.objects.all()
    serializer_class = CelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CelulaUpdateAPIView(UpdateAPIView):
    queryset = Celula.objects.all()
    serializer_class = CelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class CelulaDestroyAPIView(DestroyAPIView):
    queryset = Celula.objects.all()
    serializer_class = CelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class EstadoCelulaListAPIView(ListAPIView):
    queryset = EstadoCelula.objects.all()
    serializer_class = EstadoCelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class EstadoCelulaCreateAPIView(CreateAPIView):
    queryset = EstadoCelula.objects.all()
    serializer_class = EstadoCelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class EstadoCelulaRetrieveAPIView(RetrieveAPIView):
    queryset = EstadoCelula.objects.all()
    serializer_class = EstadoCelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class EstadoCelulaUpdateAPIView(UpdateAPIView):
    queryset = EstadoCelula.objects.all()
    serializer_class = EstadoCelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class EstadoCelulaDestroyAPIView(DestroyAPIView):
    queryset = EstadoCelula.objects.all()
    serializer_class = EstadoCelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class EvolucionCelulaListAPIView(ListAPIView):
    queryset = EvolucionCelula.objects.all()
    serializer_class = EvolucionCelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class EvolucionCelulaCreateAPIView(CreateAPIView):
    queryset = EvolucionCelula.objects.all()
    serializer_class = EvolucionCelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class EvolucionCelulaRetrieveAPIView(RetrieveAPIView):
    queryset = EvolucionCelula.objects.all()
    serializer_class = EvolucionCelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class EvolucionCelulaUpdateAPIView(UpdateAPIView):
    queryset = EvolucionCelula.objects.all()
    serializer_class = EvolucionCelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class EvolucionCelulaDestroyAPIView(DestroyAPIView):
    queryset = EvolucionCelula.objects.all()
    serializer_class = EvolucionCelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class UbicacionCelulaListAPIView(ListAPIView):
    queryset = UbicacionCelula.objects.all()
    serializer_class = UbicacionCelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class UbicacionCelulaCreateAPIView(CreateAPIView):
    queryset = UbicacionCelula.objects.all()
    serializer_class = UbicacionCelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class UbicacionCelulaRetrieveAPIView(RetrieveAPIView):
    queryset = UbicacionCelula.objects.all()
    serializer_class = UbicacionCelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class UbicacionCelulaUpdateAPIView(UpdateAPIView):
    queryset = UbicacionCelula.objects.all()
    serializer_class = UbicacionCelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class UbicacionCelulaDestroyAPIView(DestroyAPIView):
    queryset = UbicacionCelula.objects.all()
    serializer_class = UbicacionCelulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

