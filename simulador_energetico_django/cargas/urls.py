from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += [
    path('createview_carga/', Carga_CreateView.as_view(), name='Carga_CreateView'),
    path('listview_carga/', Carga_ListView.as_view(), name='Carga_ListView'),
    path('updateview_carga/<int:pk>/', Carga_UpdateView.as_view(), name='Carga_UpdateView'),
    path('detailview_carga/<int:pk>/', Carga_DetailView.as_view(), name='Carga_DetailView'),
    path('deleteview_carga/<int:pk>/', Carga_DeleteView.as_view(), name='Carga_DeleteView'),
    path('api/listapiview_carga/', CargaListAPIView.as_view(), name='Carga_ListAPIView'),
    path('api/createapiview_carga/', CargaCreateAPIView.as_view(), name='Carga_CreateAPIView'),
    path('api/retrieveapiview_carga/<int:pk>/', CargaRetrieveAPIView.as_view(), name='Carga_RetrieveAPIView'),
    path('api/updateapiview_carga/<int:pk>/', CargaUpdateAPIView.as_view(), name='Carga_UpdateAPIView'),
    path('api/destroyapiview_carga/<int:pk>/', CargaDestroyAPIView.as_view(), name='Carga_DestroyAPIView'),
]

urlpatterns += [
    path('createview_tipocarga/', TipoCarga_CreateView.as_view(), name='TipoCarga_CreateView'),
    path('listview_tipocarga/', TipoCarga_ListView.as_view(), name='TipoCarga_ListView'),
    path('updateview_tipocarga/<int:pk>/', TipoCarga_UpdateView.as_view(), name='TipoCarga_UpdateView'),
    path('detailview_tipocarga/<int:pk>/', TipoCarga_DetailView.as_view(), name='TipoCarga_DetailView'),
    path('deleteview_tipocarga/<int:pk>/', TipoCarga_DeleteView.as_view(), name='TipoCarga_DeleteView'),
    path('api/listapiview_tipocarga/', TipoCargaListAPIView.as_view(), name='TipoCarga_ListAPIView'),
    path('api/createapiview_tipocarga/', TipoCargaCreateAPIView.as_view(), name='TipoCarga_CreateAPIView'),
    path('api/retrieveapiview_tipocarga/<int:pk>/', TipoCargaRetrieveAPIView.as_view(), name='TipoCarga_RetrieveAPIView'),
    path('api/updateapiview_tipocarga/<int:pk>/', TipoCargaUpdateAPIView.as_view(), name='TipoCarga_UpdateAPIView'),
    path('api/destroyapiview_tipocarga/<int:pk>/', TipoCargaDestroyAPIView.as_view(), name='TipoCarga_DestroyAPIView'),
]
