from rest_framework.generics import *
from rest_framework import permissions
from .models import *
from .serializers import *

class ReservaEnergeticaListAPIView(ListAPIView):
    queryset = ReservaEnergetica.objects.all()
    serializer_class = ReservaEnergeticaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ReservaEnergeticaCreateAPIView(CreateAPIView):
    queryset = ReservaEnergetica.objects.all()
    serializer_class = ReservaEnergeticaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ReservaEnergeticaRetrieveAPIView(RetrieveAPIView):
    queryset = ReservaEnergetica.objects.all()
    serializer_class = ReservaEnergeticaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ReservaEnergeticaUpdateAPIView(UpdateAPIView):
    queryset = ReservaEnergetica.objects.all()
    serializer_class = ReservaEnergeticaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class ReservaEnergeticaDestroyAPIView(DestroyAPIView):
    queryset = ReservaEnergetica.objects.all()
    serializer_class = ReservaEnergeticaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class TipoReservaListAPIView(ListAPIView):
    queryset = TipoReserva.objects.all()
    serializer_class = TipoReservaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoReservaCreateAPIView(CreateAPIView):
    queryset = TipoReserva.objects.all()
    serializer_class = TipoReservaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class TipoReservaRetrieveAPIView(RetrieveAPIView):
    queryset = TipoReserva.objects.all()
    serializer_class = TipoReservaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoReservaUpdateAPIView(UpdateAPIView):
    queryset = TipoReserva.objects.all()
    serializer_class = TipoReservaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class TipoReservaDestroyAPIView(DestroyAPIView):
    queryset = TipoReserva.objects.all()
    serializer_class = TipoReservaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

