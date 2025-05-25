from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += [
    path('createview_configuracion/', Configuracion_CreateView.as_view(), name='Configuracion_CreateView'),
    path('listview_configuracion/', Configuracion_ListView.as_view(), name='Configuracion_ListView'),
    path('updateview_configuracion/<int:pk>/', Configuracion_UpdateView.as_view(), name='Configuracion_UpdateView'),
    path('detailview_configuracion/<int:pk>/', Configuracion_DetailView.as_view(), name='Configuracion_DetailView'),
    path('deleteview_configuracion/<int:pk>/', Configuracion_DeleteView.as_view(), name='Configuracion_DeleteView'),
    path('api/listapiview_configuracion/', ConfiguracionListAPIView.as_view(), name='Configuracion_ListAPIView'),
    path('api/createapiview_configuracion/', ConfiguracionCreateAPIView.as_view(), name='Configuracion_CreateAPIView'),
    path('api/retrieveapiview_configuracion/<int:pk>/', ConfiguracionRetrieveAPIView.as_view(), name='Configuracion_RetrieveAPIView'),
    path('api/updateapiview_configuracion/<int:pk>/', ConfiguracionUpdateAPIView.as_view(), name='Configuracion_UpdateAPIView'),
    path('api/destroyapiview_configuracion/<int:pk>/', ConfiguracionDestroyAPIView.as_view(), name='Configuracion_DestroyAPIView'),
]

urlpatterns += [
    path('createview_parametro/', Parametro_CreateView.as_view(), name='Parametro_CreateView'),
    path('listview_parametro/', Parametro_ListView.as_view(), name='Parametro_ListView'),
    path('updateview_parametro/<int:pk>/', Parametro_UpdateView.as_view(), name='Parametro_UpdateView'),
    path('detailview_parametro/<int:pk>/', Parametro_DetailView.as_view(), name='Parametro_DetailView'),
    path('deleteview_parametro/<int:pk>/', Parametro_DeleteView.as_view(), name='Parametro_DeleteView'),
    path('api/listapiview_parametro/', ParametroListAPIView.as_view(), name='Parametro_ListAPIView'),
    path('api/createapiview_parametro/', ParametroCreateAPIView.as_view(), name='Parametro_CreateAPIView'),
    path('api/retrieveapiview_parametro/<int:pk>/', ParametroRetrieveAPIView.as_view(), name='Parametro_RetrieveAPIView'),
    path('api/updateapiview_parametro/<int:pk>/', ParametroUpdateAPIView.as_view(), name='Parametro_UpdateAPIView'),
    path('api/destroyapiview_parametro/<int:pk>/', ParametroDestroyAPIView.as_view(), name='Parametro_DestroyAPIView'),
]

urlpatterns += [
    path('createview_log/', Log_CreateView.as_view(), name='Log_CreateView'),
    path('listview_log/', Log_ListView.as_view(), name='Log_ListView'),
    path('updateview_log/<int:pk>/', Log_UpdateView.as_view(), name='Log_UpdateView'),
    path('detailview_log/<int:pk>/', Log_DetailView.as_view(), name='Log_DetailView'),
    path('deleteview_log/<int:pk>/', Log_DeleteView.as_view(), name='Log_DeleteView'),
    path('api/listapiview_log/', LogListAPIView.as_view(), name='Log_ListAPIView'),
    path('api/createapiview_log/', LogCreateAPIView.as_view(), name='Log_CreateAPIView'),
    path('api/retrieveapiview_log/<int:pk>/', LogRetrieveAPIView.as_view(), name='Log_RetrieveAPIView'),
    path('api/updateapiview_log/<int:pk>/', LogUpdateAPIView.as_view(), name='Log_UpdateAPIView'),
    path('api/destroyapiview_log/<int:pk>/', LogDestroyAPIView.as_view(), name='Log_DestroyAPIView'),
]
