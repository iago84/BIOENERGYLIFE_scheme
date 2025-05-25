from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += [
    path('createview_generador/', Generador_CreateView.as_view(), name='Generador_CreateView'),
    path('listview_generador/', Generador_ListView.as_view(), name='Generador_ListView'),
    path('updateview_generador/<int:pk>/', Generador_UpdateView.as_view(), name='Generador_UpdateView'),
    path('detailview_generador/<int:pk>/', Generador_DetailView.as_view(), name='Generador_DetailView'),
    path('deleteview_generador/<int:pk>/', Generador_DeleteView.as_view(), name='Generador_DeleteView'),
    path('api/listapiview_generador/', GeneradorListAPIView.as_view(), name='Generador_ListAPIView'),
    path('api/createapiview_generador/', GeneradorCreateAPIView.as_view(), name='Generador_CreateAPIView'),
    path('api/retrieveapiview_generador/<int:pk>/', GeneradorRetrieveAPIView.as_view(), name='Generador_RetrieveAPIView'),
    path('api/updateapiview_generador/<int:pk>/', GeneradorUpdateAPIView.as_view(), name='Generador_UpdateAPIView'),
    path('api/destroyapiview_generador/<int:pk>/', GeneradorDestroyAPIView.as_view(), name='Generador_DestroyAPIView'),
]

urlpatterns += [
    path('createview_tipogenerador/', TipoGenerador_CreateView.as_view(), name='TipoGenerador_CreateView'),
    path('listview_tipogenerador/', TipoGenerador_ListView.as_view(), name='TipoGenerador_ListView'),
    path('updateview_tipogenerador/<int:pk>/', TipoGenerador_UpdateView.as_view(), name='TipoGenerador_UpdateView'),
    path('detailview_tipogenerador/<int:pk>/', TipoGenerador_DetailView.as_view(), name='TipoGenerador_DetailView'),
    path('deleteview_tipogenerador/<int:pk>/', TipoGenerador_DeleteView.as_view(), name='TipoGenerador_DeleteView'),
    path('api/listapiview_tipogenerador/', TipoGeneradorListAPIView.as_view(), name='TipoGenerador_ListAPIView'),
    path('api/createapiview_tipogenerador/', TipoGeneradorCreateAPIView.as_view(), name='TipoGenerador_CreateAPIView'),
    path('api/retrieveapiview_tipogenerador/<int:pk>/', TipoGeneradorRetrieveAPIView.as_view(), name='TipoGenerador_RetrieveAPIView'),
    path('api/updateapiview_tipogenerador/<int:pk>/', TipoGeneradorUpdateAPIView.as_view(), name='TipoGenerador_UpdateAPIView'),
    path('api/destroyapiview_tipogenerador/<int:pk>/', TipoGeneradorDestroyAPIView.as_view(), name='TipoGenerador_DestroyAPIView'),
]

urlpatterns += [
    path('createview_arranque/', Arranque_CreateView.as_view(), name='Arranque_CreateView'),
    path('listview_arranque/', Arranque_ListView.as_view(), name='Arranque_ListView'),
    path('updateview_arranque/<int:pk>/', Arranque_UpdateView.as_view(), name='Arranque_UpdateView'),
    path('detailview_arranque/<int:pk>/', Arranque_DetailView.as_view(), name='Arranque_DetailView'),
    path('deleteview_arranque/<int:pk>/', Arranque_DeleteView.as_view(), name='Arranque_DeleteView'),
    path('api/listapiview_arranque/', ArranqueListAPIView.as_view(), name='Arranque_ListAPIView'),
    path('api/createapiview_arranque/', ArranqueCreateAPIView.as_view(), name='Arranque_CreateAPIView'),
    path('api/retrieveapiview_arranque/<int:pk>/', ArranqueRetrieveAPIView.as_view(), name='Arranque_RetrieveAPIView'),
    path('api/updateapiview_arranque/<int:pk>/', ArranqueUpdateAPIView.as_view(), name='Arranque_UpdateAPIView'),
    path('api/destroyapiview_arranque/<int:pk>/', ArranqueDestroyAPIView.as_view(), name='Arranque_DestroyAPIView'),
]

urlpatterns += [
    path('createview_rack/', Rack_CreateView.as_view(), name='Rack_CreateView'),
    path('listview_rack/', Rack_ListView.as_view(), name='Rack_ListView'),
    path('updateview_rack/<int:pk>/', Rack_UpdateView.as_view(), name='Rack_UpdateView'),
    path('detailview_rack/<int:pk>/', Rack_DetailView.as_view(), name='Rack_DetailView'),
    path('deleteview_rack/<int:pk>/', Rack_DeleteView.as_view(), name='Rack_DeleteView'),
    path('api/listapiview_rack/', RackListAPIView.as_view(), name='Rack_ListAPIView'),
    path('api/createapiview_rack/', RackCreateAPIView.as_view(), name='Rack_CreateAPIView'),
    path('api/retrieveapiview_rack/<int:pk>/', RackRetrieveAPIView.as_view(), name='Rack_RetrieveAPIView'),
    path('api/updateapiview_rack/<int:pk>/', RackUpdateAPIView.as_view(), name='Rack_UpdateAPIView'),
    path('api/destroyapiview_rack/<int:pk>/', RackDestroyAPIView.as_view(), name='Rack_DestroyAPIView'),
]
