from rest_framework.generics import *
from rest_framework import permissions
from .models import *
from .serializers import *

class TejidoListAPIView(ListAPIView):
    queryset = Tejido.objects.all()
    serializer_class = TejidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TejidoCreateAPIView(CreateAPIView):
    queryset = Tejido.objects.all()
    serializer_class = TejidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class TejidoRetrieveAPIView(RetrieveAPIView):
    queryset = Tejido.objects.all()
    serializer_class = TejidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TejidoUpdateAPIView(UpdateAPIView):
    queryset = Tejido.objects.all()
    serializer_class = TejidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class TejidoDestroyAPIView(DestroyAPIView):
    queryset = Tejido.objects.all()
    serializer_class = TejidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class TipoTejidoListAPIView(ListAPIView):
    queryset = TipoTejido.objects.all()
    serializer_class = TipoTejidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoTejidoCreateAPIView(CreateAPIView):
    queryset = TipoTejido.objects.all()
    serializer_class = TipoTejidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class TipoTejidoRetrieveAPIView(RetrieveAPIView):
    queryset = TipoTejido.objects.all()
    serializer_class = TipoTejidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoTejidoUpdateAPIView(UpdateAPIView):
    queryset = TipoTejido.objects.all()
    serializer_class = TipoTejidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class TipoTejidoDestroyAPIView(DestroyAPIView):
    queryset = TipoTejido.objects.all()
    serializer_class = TipoTejidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

