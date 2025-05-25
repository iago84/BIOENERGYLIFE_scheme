from rest_framework.generics import *
from rest_framework import permissions
from .models import *
from .serializers import *

class GeneradorListAPIView(ListAPIView):
    queryset = Generador.objects.all()
    serializer_class = GeneradorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class GeneradorCreateAPIView(CreateAPIView):
    queryset = Generador.objects.all()
    serializer_class = GeneradorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class GeneradorRetrieveAPIView(RetrieveAPIView):
    queryset = Generador.objects.all()
    serializer_class = GeneradorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class GeneradorUpdateAPIView(UpdateAPIView):
    queryset = Generador.objects.all()
    serializer_class = GeneradorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class GeneradorDestroyAPIView(DestroyAPIView):
    queryset = Generador.objects.all()
    serializer_class = GeneradorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class TipoGeneradorListAPIView(ListAPIView):
    queryset = TipoGenerador.objects.all()
    serializer_class = TipoGeneradorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoGeneradorCreateAPIView(CreateAPIView):
    queryset = TipoGenerador.objects.all()
    serializer_class = TipoGeneradorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class TipoGeneradorRetrieveAPIView(RetrieveAPIView):
    queryset = TipoGenerador.objects.all()
    serializer_class = TipoGeneradorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoGeneradorUpdateAPIView(UpdateAPIView):
    queryset = TipoGenerador.objects.all()
    serializer_class = TipoGeneradorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class TipoGeneradorDestroyAPIView(DestroyAPIView):
    queryset = TipoGenerador.objects.all()
    serializer_class = TipoGeneradorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class ArranqueListAPIView(ListAPIView):
    queryset = Arranque.objects.all()
    serializer_class = ArranqueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ArranqueCreateAPIView(CreateAPIView):
    queryset = Arranque.objects.all()
    serializer_class = ArranqueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ArranqueRetrieveAPIView(RetrieveAPIView):
    queryset = Arranque.objects.all()
    serializer_class = ArranqueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ArranqueUpdateAPIView(UpdateAPIView):
    queryset = Arranque.objects.all()
    serializer_class = ArranqueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class ArranqueDestroyAPIView(DestroyAPIView):
    queryset = Arranque.objects.all()
    serializer_class = ArranqueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class RackListAPIView(ListAPIView):
    queryset = Rack.objects.all()
    serializer_class = RackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class RackCreateAPIView(CreateAPIView):
    queryset = Rack.objects.all()
    serializer_class = RackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class RackRetrieveAPIView(RetrieveAPIView):
    queryset = Rack.objects.all()
    serializer_class = RackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class RackUpdateAPIView(UpdateAPIView):
    queryset = Rack.objects.all()
    serializer_class = RackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class RackDestroyAPIView(DestroyAPIView):
    queryset = Rack.objects.all()
    serializer_class = RackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

