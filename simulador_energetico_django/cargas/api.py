from rest_framework.generics import *
from rest_framework import permissions
from .models import *
from .serializers import *

class CargaListAPIView(ListAPIView):
    queryset = Carga.objects.all()
    serializer_class = CargaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CargaCreateAPIView(CreateAPIView):
    queryset = Carga.objects.all()
    serializer_class = CargaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class CargaRetrieveAPIView(RetrieveAPIView):
    queryset = Carga.objects.all()
    serializer_class = CargaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CargaUpdateAPIView(UpdateAPIView):
    queryset = Carga.objects.all()
    serializer_class = CargaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class CargaDestroyAPIView(DestroyAPIView):
    queryset = Carga.objects.all()
    serializer_class = CargaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class TipoCargaListAPIView(ListAPIView):
    queryset = TipoCarga.objects.all()
    serializer_class = TipoCargaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoCargaCreateAPIView(CreateAPIView):
    queryset = TipoCarga.objects.all()
    serializer_class = TipoCargaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class TipoCargaRetrieveAPIView(RetrieveAPIView):
    queryset = TipoCarga.objects.all()
    serializer_class = TipoCargaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoCargaUpdateAPIView(UpdateAPIView):
    queryset = TipoCarga.objects.all()
    serializer_class = TipoCargaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class TipoCargaDestroyAPIView(DestroyAPIView):
    queryset = TipoCarga.objects.all()
    serializer_class = TipoCargaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

