from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += [
    path('createview_reservaenergetica/', ReservaEnergetica_CreateView.as_view(), name='ReservaEnergetica_CreateView'),
    path('listview_reservaenergetica/', ReservaEnergetica_ListView.as_view(), name='ReservaEnergetica_ListView'),
    path('updateview_reservaenergetica/<int:pk>/', ReservaEnergetica_UpdateView.as_view(), name='ReservaEnergetica_UpdateView'),
    path('detailview_reservaenergetica/<int:pk>/', ReservaEnergetica_DetailView.as_view(), name='ReservaEnergetica_DetailView'),
    path('deleteview_reservaenergetica/<int:pk>/', ReservaEnergetica_DeleteView.as_view(), name='ReservaEnergetica_DeleteView'),
    path('api/listapiview_reservaenergetica/', ReservaEnergeticaListAPIView.as_view(), name='ReservaEnergetica_ListAPIView'),
    path('api/createapiview_reservaenergetica/', ReservaEnergeticaCreateAPIView.as_view(), name='ReservaEnergetica_CreateAPIView'),
    path('api/retrieveapiview_reservaenergetica/<int:pk>/', ReservaEnergeticaRetrieveAPIView.as_view(), name='ReservaEnergetica_RetrieveAPIView'),
    path('api/updateapiview_reservaenergetica/<int:pk>/', ReservaEnergeticaUpdateAPIView.as_view(), name='ReservaEnergetica_UpdateAPIView'),
    path('api/destroyapiview_reservaenergetica/<int:pk>/', ReservaEnergeticaDestroyAPIView.as_view(), name='ReservaEnergetica_DestroyAPIView'),
]

urlpatterns += [
    path('createview_tiporeserva/', TipoReserva_CreateView.as_view(), name='TipoReserva_CreateView'),
    path('listview_tiporeserva/', TipoReserva_ListView.as_view(), name='TipoReserva_ListView'),
    path('updateview_tiporeserva/<int:pk>/', TipoReserva_UpdateView.as_view(), name='TipoReserva_UpdateView'),
    path('detailview_tiporeserva/<int:pk>/', TipoReserva_DetailView.as_view(), name='TipoReserva_DetailView'),
    path('deleteview_tiporeserva/<int:pk>/', TipoReserva_DeleteView.as_view(), name='TipoReserva_DeleteView'),
    path('api/listapiview_tiporeserva/', TipoReservaListAPIView.as_view(), name='TipoReserva_ListAPIView'),
    path('api/createapiview_tiporeserva/', TipoReservaCreateAPIView.as_view(), name='TipoReserva_CreateAPIView'),
    path('api/retrieveapiview_tiporeserva/<int:pk>/', TipoReservaRetrieveAPIView.as_view(), name='TipoReserva_RetrieveAPIView'),
    path('api/updateapiview_tiporeserva/<int:pk>/', TipoReservaUpdateAPIView.as_view(), name='TipoReserva_UpdateAPIView'),
    path('api/destroyapiview_tiporeserva/<int:pk>/', TipoReservaDestroyAPIView.as_view(), name='TipoReserva_DestroyAPIView'),
]
