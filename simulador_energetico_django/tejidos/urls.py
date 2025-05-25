from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += [
    path('createview_tejido/', Tejido_CreateView.as_view(), name='Tejido_CreateView'),
    path('listview_tejido/', Tejido_ListView.as_view(), name='Tejido_ListView'),
    path('updateview_tejido/<int:pk>/', Tejido_UpdateView.as_view(), name='Tejido_UpdateView'),
    path('detailview_tejido/<int:pk>/', Tejido_DetailView.as_view(), name='Tejido_DetailView'),
    path('deleteview_tejido/<int:pk>/', Tejido_DeleteView.as_view(), name='Tejido_DeleteView'),
    path('api/listapiview_tejido/', TejidoListAPIView.as_view(), name='Tejido_ListAPIView'),
    path('api/createapiview_tejido/', TejidoCreateAPIView.as_view(), name='Tejido_CreateAPIView'),
    path('api/retrieveapiview_tejido/<int:pk>/', TejidoRetrieveAPIView.as_view(), name='Tejido_RetrieveAPIView'),
    path('api/updateapiview_tejido/<int:pk>/', TejidoUpdateAPIView.as_view(), name='Tejido_UpdateAPIView'),
    path('api/destroyapiview_tejido/<int:pk>/', TejidoDestroyAPIView.as_view(), name='Tejido_DestroyAPIView'),
]

urlpatterns += [
    path('createview_tipotejido/', TipoTejido_CreateView.as_view(), name='TipoTejido_CreateView'),
    path('listview_tipotejido/', TipoTejido_ListView.as_view(), name='TipoTejido_ListView'),
    path('updateview_tipotejido/<int:pk>/', TipoTejido_UpdateView.as_view(), name='TipoTejido_UpdateView'),
    path('detailview_tipotejido/<int:pk>/', TipoTejido_DetailView.as_view(), name='TipoTejido_DetailView'),
    path('deleteview_tipotejido/<int:pk>/', TipoTejido_DeleteView.as_view(), name='TipoTejido_DeleteView'),
    path('api/listapiview_tipotejido/', TipoTejidoListAPIView.as_view(), name='TipoTejido_ListAPIView'),
    path('api/createapiview_tipotejido/', TipoTejidoCreateAPIView.as_view(), name='TipoTejido_CreateAPIView'),
    path('api/retrieveapiview_tipotejido/<int:pk>/', TipoTejidoRetrieveAPIView.as_view(), name='TipoTejido_RetrieveAPIView'),
    path('api/updateapiview_tipotejido/<int:pk>/', TipoTejidoUpdateAPIView.as_view(), name='TipoTejido_UpdateAPIView'),
    path('api/destroyapiview_tipotejido/<int:pk>/', TipoTejidoDestroyAPIView.as_view(), name='TipoTejido_DestroyAPIView'),
]
