from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += [
    path('createview_simulacion/', Simulacion_CreateView.as_view(), name='Simulacion_CreateView'),
    path('listview_simulacion/', Simulacion_ListView.as_view(), name='Simulacion_ListView'),
    path('updateview_simulacion/<int:pk>/', Simulacion_UpdateView.as_view(), name='Simulacion_UpdateView'),
    path('detailview_simulacion/<int:pk>/', Simulacion_DetailView.as_view(), name='Simulacion_DetailView'),
    path('deleteview_simulacion/<int:pk>/', Simulacion_DeleteView.as_view(), name='Simulacion_DeleteView'),
    path('api/listapiview_simulacion/', SimulacionListAPIView.as_view(), name='Simulacion_ListAPIView'),
    path('api/createapiview_simulacion/', SimulacionCreateAPIView.as_view(), name='Simulacion_CreateAPIView'),
    path('api/retrieveapiview_simulacion/<int:pk>/', SimulacionRetrieveAPIView.as_view(), name='Simulacion_RetrieveAPIView'),
    path('api/updateapiview_simulacion/<int:pk>/', SimulacionUpdateAPIView.as_view(), name='Simulacion_UpdateAPIView'),
    path('api/destroyapiview_simulacion/<int:pk>/', SimulacionDestroyAPIView.as_view(), name='Simulacion_DestroyAPIView'),
]

urlpatterns += [
    path('createview_resultadosimulacion/', ResultadoSimulacion_CreateView.as_view(), name='ResultadoSimulacion_CreateView'),
    path('listview_resultadosimulacion/', ResultadoSimulacion_ListView.as_view(), name='ResultadoSimulacion_ListView'),
    path('updateview_resultadosimulacion/<int:pk>/', ResultadoSimulacion_UpdateView.as_view(), name='ResultadoSimulacion_UpdateView'),
    path('detailview_resultadosimulacion/<int:pk>/', ResultadoSimulacion_DetailView.as_view(), name='ResultadoSimulacion_DetailView'),
    path('deleteview_resultadosimulacion/<int:pk>/', ResultadoSimulacion_DeleteView.as_view(), name='ResultadoSimulacion_DeleteView'),
    path('api/listapiview_resultadosimulacion/', ResultadoSimulacionListAPIView.as_view(), name='ResultadoSimulacion_ListAPIView'),
    path('api/createapiview_resultadosimulacion/', ResultadoSimulacionCreateAPIView.as_view(), name='ResultadoSimulacion_CreateAPIView'),
    path('api/retrieveapiview_resultadosimulacion/<int:pk>/', ResultadoSimulacionRetrieveAPIView.as_view(), name='ResultadoSimulacion_RetrieveAPIView'),
    path('api/updateapiview_resultadosimulacion/<int:pk>/', ResultadoSimulacionUpdateAPIView.as_view(), name='ResultadoSimulacion_UpdateAPIView'),
    path('api/destroyapiview_resultadosimulacion/<int:pk>/', ResultadoSimulacionDestroyAPIView.as_view(), name='ResultadoSimulacion_DestroyAPIView'),
]
