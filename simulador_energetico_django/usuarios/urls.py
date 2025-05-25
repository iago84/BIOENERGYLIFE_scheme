from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += [
    path('createview_usuario/', Usuario_CreateView.as_view(), name='Usuario_CreateView'),
    path('listview_usuario/', Usuario_ListView.as_view(), name='Usuario_ListView'),
    path('updateview_usuario/<int:pk>/', Usuario_UpdateView.as_view(), name='Usuario_UpdateView'),
    path('detailview_usuario/<int:pk>/', Usuario_DetailView.as_view(), name='Usuario_DetailView'),
    path('deleteview_usuario/<int:pk>/', Usuario_DeleteView.as_view(), name='Usuario_DeleteView'),
    path('api/listapiview_usuario/', UsuarioListAPIView.as_view(), name='Usuario_ListAPIView'),
    path('api/createapiview_usuario/', UsuarioCreateAPIView.as_view(), name='Usuario_CreateAPIView'),
    path('api/retrieveapiview_usuario/<int:pk>/', UsuarioRetrieveAPIView.as_view(), name='Usuario_RetrieveAPIView'),
    path('api/updateapiview_usuario/<int:pk>/', UsuarioUpdateAPIView.as_view(), name='Usuario_UpdateAPIView'),
    path('api/destroyapiview_usuario/<int:pk>/', UsuarioDestroyAPIView.as_view(), name='Usuario_DestroyAPIView'),
]

urlpatterns += [
    path('createview_perfilusuario/', PerfilUsuario_CreateView.as_view(), name='PerfilUsuario_CreateView'),
    path('listview_perfilusuario/', PerfilUsuario_ListView.as_view(), name='PerfilUsuario_ListView'),
    path('updateview_perfilusuario/<int:pk>/', PerfilUsuario_UpdateView.as_view(), name='PerfilUsuario_UpdateView'),
    path('detailview_perfilusuario/<int:pk>/', PerfilUsuario_DetailView.as_view(), name='PerfilUsuario_DetailView'),
    path('deleteview_perfilusuario/<int:pk>/', PerfilUsuario_DeleteView.as_view(), name='PerfilUsuario_DeleteView'),
    path('api/listapiview_perfilusuario/', PerfilUsuarioListAPIView.as_view(), name='PerfilUsuario_ListAPIView'),
    path('api/createapiview_perfilusuario/', PerfilUsuarioCreateAPIView.as_view(), name='PerfilUsuario_CreateAPIView'),
    path('api/retrieveapiview_perfilusuario/<int:pk>/', PerfilUsuarioRetrieveAPIView.as_view(), name='PerfilUsuario_RetrieveAPIView'),
    path('api/updateapiview_perfilusuario/<int:pk>/', PerfilUsuarioUpdateAPIView.as_view(), name='PerfilUsuario_UpdateAPIView'),
    path('api/destroyapiview_perfilusuario/<int:pk>/', PerfilUsuarioDestroyAPIView.as_view(), name='PerfilUsuario_DestroyAPIView'),
]
