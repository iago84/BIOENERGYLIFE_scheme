from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += [
    path('createview_conexion/', Conexion_CreateView.as_view(), name='Conexion_CreateView'),
    path('listview_conexion/', Conexion_ListView.as_view(), name='Conexion_ListView'),
    path('updateview_conexion/<int:pk>/', Conexion_UpdateView.as_view(), name='Conexion_UpdateView'),
    path('detailview_conexion/<int:pk>/', Conexion_DetailView.as_view(), name='Conexion_DetailView'),
    path('deleteview_conexion/<int:pk>/', Conexion_DeleteView.as_view(), name='Conexion_DeleteView'),
    path('api/listapiview_conexion/', ConexionListAPIView.as_view(), name='Conexion_ListAPIView'),
    path('api/createapiview_conexion/', ConexionCreateAPIView.as_view(), name='Conexion_CreateAPIView'),
    path('api/retrieveapiview_conexion/<int:pk>/', ConexionRetrieveAPIView.as_view(), name='Conexion_RetrieveAPIView'),
    path('api/updateapiview_conexion/<int:pk>/', ConexionUpdateAPIView.as_view(), name='Conexion_UpdateAPIView'),
    path('api/destroyapiview_conexion/<int:pk>/', ConexionDestroyAPIView.as_view(), name='Conexion_DestroyAPIView'),
]

urlpatterns += [
    path('createview_tipoconexion/', TipoConexion_CreateView.as_view(), name='TipoConexion_CreateView'),
    path('listview_tipoconexion/', TipoConexion_ListView.as_view(), name='TipoConexion_ListView'),
    path('updateview_tipoconexion/<int:pk>/', TipoConexion_UpdateView.as_view(), name='TipoConexion_UpdateView'),
    path('detailview_tipoconexion/<int:pk>/', TipoConexion_DetailView.as_view(), name='TipoConexion_DetailView'),
    path('deleteview_tipoconexion/<int:pk>/', TipoConexion_DeleteView.as_view(), name='TipoConexion_DeleteView'),
    path('api/listapiview_tipoconexion/', TipoConexionListAPIView.as_view(), name='TipoConexion_ListAPIView'),
    path('api/createapiview_tipoconexion/', TipoConexionCreateAPIView.as_view(), name='TipoConexion_CreateAPIView'),
    path('api/retrieveapiview_tipoconexion/<int:pk>/', TipoConexionRetrieveAPIView.as_view(), name='TipoConexion_RetrieveAPIView'),
    path('api/updateapiview_tipoconexion/<int:pk>/', TipoConexionUpdateAPIView.as_view(), name='TipoConexion_UpdateAPIView'),
    path('api/destroyapiview_tipoconexion/<int:pk>/', TipoConexionDestroyAPIView.as_view(), name='TipoConexion_DestroyAPIView'),
]
