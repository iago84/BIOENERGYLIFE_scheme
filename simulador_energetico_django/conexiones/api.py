from rest_framework.generics import *
from rest_framework import permissions
from .models import *
from .serializers import *

class ConexionListAPIView(ListAPIView):
    queryset = Conexion.objects.all()
    serializer_class = ConexionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ConexionCreateAPIView(CreateAPIView):
    queryset = Conexion.objects.all()
    serializer_class = ConexionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ConexionRetrieveAPIView(RetrieveAPIView):
    queryset = Conexion.objects.all()
    serializer_class = ConexionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ConexionUpdateAPIView(UpdateAPIView):
    queryset = Conexion.objects.all()
    serializer_class = ConexionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class ConexionDestroyAPIView(DestroyAPIView):
    queryset = Conexion.objects.all()
    serializer_class = ConexionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class TipoConexionListAPIView(ListAPIView):
    queryset = TipoConexion.objects.all()
    serializer_class = TipoConexionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoConexionCreateAPIView(CreateAPIView):
    queryset = TipoConexion.objects.all()
    serializer_class = TipoConexionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class TipoConexionRetrieveAPIView(RetrieveAPIView):
    queryset = TipoConexion.objects.all()
    serializer_class = TipoConexionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoConexionUpdateAPIView(UpdateAPIView):
    queryset = TipoConexion.objects.all()
    serializer_class = TipoConexionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class TipoConexionDestroyAPIView(DestroyAPIView):
    queryset = TipoConexion.objects.all()
    serializer_class = TipoConexionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

