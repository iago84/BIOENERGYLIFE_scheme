from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += [
    path('createview_sensor/', Sensor_CreateView.as_view(), name='Sensor_CreateView'),
    path('listview_sensor/', Sensor_ListView.as_view(), name='Sensor_ListView'),
    path('updateview_sensor/<int:pk>/', Sensor_UpdateView.as_view(), name='Sensor_UpdateView'),
    path('detailview_sensor/<int:pk>/', Sensor_DetailView.as_view(), name='Sensor_DetailView'),
    path('deleteview_sensor/<int:pk>/', Sensor_DeleteView.as_view(), name='Sensor_DeleteView'),
    path('api/listapiview_sensor/', SensorListAPIView.as_view(), name='Sensor_ListAPIView'),
    path('api/createapiview_sensor/', SensorCreateAPIView.as_view(), name='Sensor_CreateAPIView'),
    path('api/retrieveapiview_sensor/<int:pk>/', SensorRetrieveAPIView.as_view(), name='Sensor_RetrieveAPIView'),
    path('api/updateapiview_sensor/<int:pk>/', SensorUpdateAPIView.as_view(), name='Sensor_UpdateAPIView'),
    path('api/destroyapiview_sensor/<int:pk>/', SensorDestroyAPIView.as_view(), name='Sensor_DestroyAPIView'),
]

urlpatterns += [
    path('createview_medidor/', Medidor_CreateView.as_view(), name='Medidor_CreateView'),
    path('listview_medidor/', Medidor_ListView.as_view(), name='Medidor_ListView'),
    path('updateview_medidor/<int:pk>/', Medidor_UpdateView.as_view(), name='Medidor_UpdateView'),
    path('detailview_medidor/<int:pk>/', Medidor_DetailView.as_view(), name='Medidor_DetailView'),
    path('deleteview_medidor/<int:pk>/', Medidor_DeleteView.as_view(), name='Medidor_DeleteView'),
    path('api/listapiview_medidor/', MedidorListAPIView.as_view(), name='Medidor_ListAPIView'),
    path('api/createapiview_medidor/', MedidorCreateAPIView.as_view(), name='Medidor_CreateAPIView'),
    path('api/retrieveapiview_medidor/<int:pk>/', MedidorRetrieveAPIView.as_view(), name='Medidor_RetrieveAPIView'),
    path('api/updateapiview_medidor/<int:pk>/', MedidorUpdateAPIView.as_view(), name='Medidor_UpdateAPIView'),
    path('api/destroyapiview_medidor/<int:pk>/', MedidorDestroyAPIView.as_view(), name='Medidor_DestroyAPIView'),
]

urlpatterns += [
    path('createview_tiposensor/', TipoSensor_CreateView.as_view(), name='TipoSensor_CreateView'),
    path('listview_tiposensor/', TipoSensor_ListView.as_view(), name='TipoSensor_ListView'),
    path('updateview_tiposensor/<int:pk>/', TipoSensor_UpdateView.as_view(), name='TipoSensor_UpdateView'),
    path('detailview_tiposensor/<int:pk>/', TipoSensor_DetailView.as_view(), name='TipoSensor_DetailView'),
    path('deleteview_tiposensor/<int:pk>/', TipoSensor_DeleteView.as_view(), name='TipoSensor_DeleteView'),
    path('api/listapiview_tiposensor/', TipoSensorListAPIView.as_view(), name='TipoSensor_ListAPIView'),
    path('api/createapiview_tiposensor/', TipoSensorCreateAPIView.as_view(), name='TipoSensor_CreateAPIView'),
    path('api/retrieveapiview_tiposensor/<int:pk>/', TipoSensorRetrieveAPIView.as_view(), name='TipoSensor_RetrieveAPIView'),
    path('api/updateapiview_tiposensor/<int:pk>/', TipoSensorUpdateAPIView.as_view(), name='TipoSensor_UpdateAPIView'),
    path('api/destroyapiview_tiposensor/<int:pk>/', TipoSensorDestroyAPIView.as_view(), name='TipoSensor_DestroyAPIView'),
]
