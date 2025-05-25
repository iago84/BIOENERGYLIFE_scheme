from rest_framework.generics import *
from rest_framework import permissions
from .models import *
from .serializers import *

class OrganuloListAPIView(ListAPIView):
    queryset = Organulo.objects.all()
    serializer_class = OrganuloSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class OrganuloCreateAPIView(CreateAPIView):
    queryset = Organulo.objects.all()
    serializer_class = OrganuloSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class OrganuloRetrieveAPIView(RetrieveAPIView):
    queryset = Organulo.objects.all()
    serializer_class = OrganuloSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class OrganuloUpdateAPIView(UpdateAPIView):
    queryset = Organulo.objects.all()
    serializer_class = OrganuloSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class OrganuloDestroyAPIView(DestroyAPIView):
    queryset = Organulo.objects.all()
    serializer_class = OrganuloSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class TipoOrganuloListAPIView(ListAPIView):
    queryset = TipoOrganulo.objects.all()
    serializer_class = TipoOrganuloSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoOrganuloCreateAPIView(CreateAPIView):
    queryset = TipoOrganulo.objects.all()
    serializer_class = TipoOrganuloSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class TipoOrganuloRetrieveAPIView(RetrieveAPIView):
    queryset = TipoOrganulo.objects.all()
    serializer_class = TipoOrganuloSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TipoOrganuloUpdateAPIView(UpdateAPIView):
    queryset = TipoOrganulo.objects.all()
    serializer_class = TipoOrganuloSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class TipoOrganuloDestroyAPIView(DestroyAPIView):
    queryset = TipoOrganulo.objects.all()
    serializer_class = TipoOrganuloSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class SecuenciadorListAPIView(ListAPIView):
    queryset = Secuenciador.objects.all()
    serializer_class = SecuenciadorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class SecuenciadorCreateAPIView(CreateAPIView):
    queryset = Secuenciador.objects.all()
    serializer_class = SecuenciadorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class SecuenciadorRetrieveAPIView(RetrieveAPIView):
    queryset = Secuenciador.objects.all()
    serializer_class = SecuenciadorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class SecuenciadorUpdateAPIView(UpdateAPIView):
    queryset = Secuenciador.objects.all()
    serializer_class = SecuenciadorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class SecuenciadorDestroyAPIView(DestroyAPIView):
    queryset = Secuenciador.objects.all()
    serializer_class = SecuenciadorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class DispositivoControlListAPIView(ListAPIView):
    queryset = DispositivoControl.objects.all()
    serializer_class = DispositivoControlSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class DispositivoControlCreateAPIView(CreateAPIView):
    queryset = DispositivoControl.objects.all()
    serializer_class = DispositivoControlSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class DispositivoControlRetrieveAPIView(RetrieveAPIView):
    queryset = DispositivoControl.objects.all()
    serializer_class = DispositivoControlSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class DispositivoControlUpdateAPIView(UpdateAPIView):
    queryset = DispositivoControl.objects.all()
    serializer_class = DispositivoControlSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class DispositivoControlDestroyAPIView(DestroyAPIView):
    queryset = DispositivoControl.objects.all()
    serializer_class = DispositivoControlSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

