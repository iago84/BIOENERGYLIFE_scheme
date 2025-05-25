from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += [
    path('createview_organulo/', Organulo_CreateView.as_view(), name='Organulo_CreateView'),
    path('listview_organulo/', Organulo_ListView.as_view(), name='Organulo_ListView'),
    path('updateview_organulo/<int:pk>/', Organulo_UpdateView.as_view(), name='Organulo_UpdateView'),
    path('detailview_organulo/<int:pk>/', Organulo_DetailView.as_view(), name='Organulo_DetailView'),
    path('deleteview_organulo/<int:pk>/', Organulo_DeleteView.as_view(), name='Organulo_DeleteView'),
    path('api/listapiview_organulo/', OrganuloListAPIView.as_view(), name='Organulo_ListAPIView'),
    path('api/createapiview_organulo/', OrganuloCreateAPIView.as_view(), name='Organulo_CreateAPIView'),
    path('api/retrieveapiview_organulo/<int:pk>/', OrganuloRetrieveAPIView.as_view(), name='Organulo_RetrieveAPIView'),
    path('api/updateapiview_organulo/<int:pk>/', OrganuloUpdateAPIView.as_view(), name='Organulo_UpdateAPIView'),
    path('api/destroyapiview_organulo/<int:pk>/', OrganuloDestroyAPIView.as_view(), name='Organulo_DestroyAPIView'),
]

urlpatterns += [
    path('createview_tipoorganulo/', TipoOrganulo_CreateView.as_view(), name='TipoOrganulo_CreateView'),
    path('listview_tipoorganulo/', TipoOrganulo_ListView.as_view(), name='TipoOrganulo_ListView'),
    path('updateview_tipoorganulo/<int:pk>/', TipoOrganulo_UpdateView.as_view(), name='TipoOrganulo_UpdateView'),
    path('detailview_tipoorganulo/<int:pk>/', TipoOrganulo_DetailView.as_view(), name='TipoOrganulo_DetailView'),
    path('deleteview_tipoorganulo/<int:pk>/', TipoOrganulo_DeleteView.as_view(), name='TipoOrganulo_DeleteView'),
    path('api/listapiview_tipoorganulo/', TipoOrganuloListAPIView.as_view(), name='TipoOrganulo_ListAPIView'),
    path('api/createapiview_tipoorganulo/', TipoOrganuloCreateAPIView.as_view(), name='TipoOrganulo_CreateAPIView'),
    path('api/retrieveapiview_tipoorganulo/<int:pk>/', TipoOrganuloRetrieveAPIView.as_view(), name='TipoOrganulo_RetrieveAPIView'),
    path('api/updateapiview_tipoorganulo/<int:pk>/', TipoOrganuloUpdateAPIView.as_view(), name='TipoOrganulo_UpdateAPIView'),
    path('api/destroyapiview_tipoorganulo/<int:pk>/', TipoOrganuloDestroyAPIView.as_view(), name='TipoOrganulo_DestroyAPIView'),
]

urlpatterns += [
    path('createview_secuenciador/', Secuenciador_CreateView.as_view(), name='Secuenciador_CreateView'),
    path('listview_secuenciador/', Secuenciador_ListView.as_view(), name='Secuenciador_ListView'),
    path('updateview_secuenciador/<int:pk>/', Secuenciador_UpdateView.as_view(), name='Secuenciador_UpdateView'),
    path('detailview_secuenciador/<int:pk>/', Secuenciador_DetailView.as_view(), name='Secuenciador_DetailView'),
    path('deleteview_secuenciador/<int:pk>/', Secuenciador_DeleteView.as_view(), name='Secuenciador_DeleteView'),
    path('api/listapiview_secuenciador/', SecuenciadorListAPIView.as_view(), name='Secuenciador_ListAPIView'),
    path('api/createapiview_secuenciador/', SecuenciadorCreateAPIView.as_view(), name='Secuenciador_CreateAPIView'),
    path('api/retrieveapiview_secuenciador/<int:pk>/', SecuenciadorRetrieveAPIView.as_view(), name='Secuenciador_RetrieveAPIView'),
    path('api/updateapiview_secuenciador/<int:pk>/', SecuenciadorUpdateAPIView.as_view(), name='Secuenciador_UpdateAPIView'),
    path('api/destroyapiview_secuenciador/<int:pk>/', SecuenciadorDestroyAPIView.as_view(), name='Secuenciador_DestroyAPIView'),
]

urlpatterns += [
    path('createview_dispositivocontrol/', DispositivoControl_CreateView.as_view(), name='DispositivoControl_CreateView'),
    path('listview_dispositivocontrol/', DispositivoControl_ListView.as_view(), name='DispositivoControl_ListView'),
    path('updateview_dispositivocontrol/<int:pk>/', DispositivoControl_UpdateView.as_view(), name='DispositivoControl_UpdateView'),
    path('detailview_dispositivocontrol/<int:pk>/', DispositivoControl_DetailView.as_view(), name='DispositivoControl_DetailView'),
    path('deleteview_dispositivocontrol/<int:pk>/', DispositivoControl_DeleteView.as_view(), name='DispositivoControl_DeleteView'),
    path('api/listapiview_dispositivocontrol/', DispositivoControlListAPIView.as_view(), name='DispositivoControl_ListAPIView'),
    path('api/createapiview_dispositivocontrol/', DispositivoControlCreateAPIView.as_view(), name='DispositivoControl_CreateAPIView'),
    path('api/retrieveapiview_dispositivocontrol/<int:pk>/', DispositivoControlRetrieveAPIView.as_view(), name='DispositivoControl_RetrieveAPIView'),
    path('api/updateapiview_dispositivocontrol/<int:pk>/', DispositivoControlUpdateAPIView.as_view(), name='DispositivoControl_UpdateAPIView'),
    path('api/destroyapiview_dispositivocontrol/<int:pk>/', DispositivoControlDestroyAPIView.as_view(), name='DispositivoControl_DestroyAPIView'),
]
