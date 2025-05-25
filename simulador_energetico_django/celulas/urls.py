from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += [
    path('createview_celula/', Celula_CreateView.as_view(), name='Celula_CreateView'),
    path('listview_celula/', Celula_ListView.as_view(), name='Celula_ListView'),
    path('updateview_celula/<int:pk>/', Celula_UpdateView.as_view(), name='Celula_UpdateView'),
    path('detailview_celula/<int:pk>/', Celula_DetailView.as_view(), name='Celula_DetailView'),
    path('deleteview_celula/<int:pk>/', Celula_DeleteView.as_view(), name='Celula_DeleteView'),
    path('api/listapiview_celula/', CelulaListAPIView.as_view(), name='Celula_ListAPIView'),
    path('api/createapiview_celula/', CelulaCreateAPIView.as_view(), name='Celula_CreateAPIView'),
    path('api/retrieveapiview_celula/<int:pk>/', CelulaRetrieveAPIView.as_view(), name='Celula_RetrieveAPIView'),
    path('api/updateapiview_celula/<int:pk>/', CelulaUpdateAPIView.as_view(), name='Celula_UpdateAPIView'),
    path('api/destroyapiview_celula/<int:pk>/', CelulaDestroyAPIView.as_view(), name='Celula_DestroyAPIView'),
]

urlpatterns += [
    path('createview_estadocelula/', EstadoCelula_CreateView.as_view(), name='EstadoCelula_CreateView'),
    path('listview_estadocelula/', EstadoCelula_ListView.as_view(), name='EstadoCelula_ListView'),
    path('updateview_estadocelula/<int:pk>/', EstadoCelula_UpdateView.as_view(), name='EstadoCelula_UpdateView'),
    path('detailview_estadocelula/<int:pk>/', EstadoCelula_DetailView.as_view(), name='EstadoCelula_DetailView'),
    path('deleteview_estadocelula/<int:pk>/', EstadoCelula_DeleteView.as_view(), name='EstadoCelula_DeleteView'),
    path('api/listapiview_estadocelula/', EstadoCelulaListAPIView.as_view(), name='EstadoCelula_ListAPIView'),
    path('api/createapiview_estadocelula/', EstadoCelulaCreateAPIView.as_view(), name='EstadoCelula_CreateAPIView'),
    path('api/retrieveapiview_estadocelula/<int:pk>/', EstadoCelulaRetrieveAPIView.as_view(), name='EstadoCelula_RetrieveAPIView'),
    path('api/updateapiview_estadocelula/<int:pk>/', EstadoCelulaUpdateAPIView.as_view(), name='EstadoCelula_UpdateAPIView'),
    path('api/destroyapiview_estadocelula/<int:pk>/', EstadoCelulaDestroyAPIView.as_view(), name='EstadoCelula_DestroyAPIView'),
]

urlpatterns += [
    path('createview_evolucioncelula/', EvolucionCelula_CreateView.as_view(), name='EvolucionCelula_CreateView'),
    path('listview_evolucioncelula/', EvolucionCelula_ListView.as_view(), name='EvolucionCelula_ListView'),
    path('updateview_evolucioncelula/<int:pk>/', EvolucionCelula_UpdateView.as_view(), name='EvolucionCelula_UpdateView'),
    path('detailview_evolucioncelula/<int:pk>/', EvolucionCelula_DetailView.as_view(), name='EvolucionCelula_DetailView'),
    path('deleteview_evolucioncelula/<int:pk>/', EvolucionCelula_DeleteView.as_view(), name='EvolucionCelula_DeleteView'),
    path('api/listapiview_evolucioncelula/', EvolucionCelulaListAPIView.as_view(), name='EvolucionCelula_ListAPIView'),
    path('api/createapiview_evolucioncelula/', EvolucionCelulaCreateAPIView.as_view(), name='EvolucionCelula_CreateAPIView'),
    path('api/retrieveapiview_evolucioncelula/<int:pk>/', EvolucionCelulaRetrieveAPIView.as_view(), name='EvolucionCelula_RetrieveAPIView'),
    path('api/updateapiview_evolucioncelula/<int:pk>/', EvolucionCelulaUpdateAPIView.as_view(), name='EvolucionCelula_UpdateAPIView'),
    path('api/destroyapiview_evolucioncelula/<int:pk>/', EvolucionCelulaDestroyAPIView.as_view(), name='EvolucionCelula_DestroyAPIView'),
]

urlpatterns += [
    path('createview_ubicacioncelula/', UbicacionCelula_CreateView.as_view(), name='UbicacionCelula_CreateView'),
    path('listview_ubicacioncelula/', UbicacionCelula_ListView.as_view(), name='UbicacionCelula_ListView'),
    path('updateview_ubicacioncelula/<int:pk>/', UbicacionCelula_UpdateView.as_view(), name='UbicacionCelula_UpdateView'),
    path('detailview_ubicacioncelula/<int:pk>/', UbicacionCelula_DetailView.as_view(), name='UbicacionCelula_DetailView'),
    path('deleteview_ubicacioncelula/<int:pk>/', UbicacionCelula_DeleteView.as_view(), name='UbicacionCelula_DeleteView'),
    path('api/listapiview_ubicacioncelula/', UbicacionCelulaListAPIView.as_view(), name='UbicacionCelula_ListAPIView'),
    path('api/createapiview_ubicacioncelula/', UbicacionCelulaCreateAPIView.as_view(), name='UbicacionCelula_CreateAPIView'),
    path('api/retrieveapiview_ubicacioncelula/<int:pk>/', UbicacionCelulaRetrieveAPIView.as_view(), name='UbicacionCelula_RetrieveAPIView'),
    path('api/updateapiview_ubicacioncelula/<int:pk>/', UbicacionCelulaUpdateAPIView.as_view(), name='UbicacionCelula_UpdateAPIView'),
    path('api/destroyapiview_ubicacioncelula/<int:pk>/', UbicacionCelulaDestroyAPIView.as_view(), name='UbicacionCelula_DestroyAPIView'),
]
