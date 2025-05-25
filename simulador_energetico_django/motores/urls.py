from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += [
    path('createview_motor/', Motor_CreateView.as_view(), name='Motor_CreateView'),
    path('listview_motor/', Motor_ListView.as_view(), name='Motor_ListView'),
    path('updateview_motor/<int:pk>/', Motor_UpdateView.as_view(), name='Motor_UpdateView'),
    path('detailview_motor/<int:pk>/', Motor_DetailView.as_view(), name='Motor_DetailView'),
    path('deleteview_motor/<int:pk>/', Motor_DeleteView.as_view(), name='Motor_DeleteView'),
    path('api/listapiview_motor/', MotorListAPIView.as_view(), name='Motor_ListAPIView'),
    path('api/createapiview_motor/', MotorCreateAPIView.as_view(), name='Motor_CreateAPIView'),
    path('api/retrieveapiview_motor/<int:pk>/', MotorRetrieveAPIView.as_view(), name='Motor_RetrieveAPIView'),
    path('api/updateapiview_motor/<int:pk>/', MotorUpdateAPIView.as_view(), name='Motor_UpdateAPIView'),
    path('api/destroyapiview_motor/<int:pk>/', MotorDestroyAPIView.as_view(), name='Motor_DestroyAPIView'),
]

urlpatterns += [
    path('createview_tipomotor/', TipoMotor_CreateView.as_view(), name='TipoMotor_CreateView'),
    path('listview_tipomotor/', TipoMotor_ListView.as_view(), name='TipoMotor_ListView'),
    path('updateview_tipomotor/<int:pk>/', TipoMotor_UpdateView.as_view(), name='TipoMotor_UpdateView'),
    path('detailview_tipomotor/<int:pk>/', TipoMotor_DetailView.as_view(), name='TipoMotor_DetailView'),
    path('deleteview_tipomotor/<int:pk>/', TipoMotor_DeleteView.as_view(), name='TipoMotor_DeleteView'),
    path('api/listapiview_tipomotor/', TipoMotorListAPIView.as_view(), name='TipoMotor_ListAPIView'),
    path('api/createapiview_tipomotor/', TipoMotorCreateAPIView.as_view(), name='TipoMotor_CreateAPIView'),
    path('api/retrieveapiview_tipomotor/<int:pk>/', TipoMotorRetrieveAPIView.as_view(), name='TipoMotor_RetrieveAPIView'),
    path('api/updateapiview_tipomotor/<int:pk>/', TipoMotorUpdateAPIView.as_view(), name='TipoMotor_UpdateAPIView'),
    path('api/destroyapiview_tipomotor/<int:pk>/', TipoMotorDestroyAPIView.as_view(), name='TipoMotor_DestroyAPIView'),
]
