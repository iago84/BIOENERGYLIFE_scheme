"""
URL configuration for simulador_energetico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]
import core.urls as core_urls

# Automatically added app include
urlpatterns.append(path('', include(core_urls)))
import celulas.urls as celulas_urls

# Automatically added app include
urlpatterns.append(path('', include(celulas_urls)))
import organulos.urls as organulos_urls

# Automatically added app include
urlpatterns.append(path('', include(organulos_urls)))
import generadores.urls as generadores_urls

# Automatically added app include
urlpatterns.append(path('', include(generadores_urls)))
import motores.urls as motores_urls

# Automatically added app include
urlpatterns.append(path('', include(motores_urls)))
import sensores.urls as sensores_urls

# Automatically added app include
urlpatterns.append(path('', include(sensores_urls)))
import almacenamiento.urls as almacenamiento_urls

# Automatically added app include
urlpatterns.append(path('', include(almacenamiento_urls)))
import cargas.urls as cargas_urls

# Automatically added app include
urlpatterns.append(path('', include(cargas_urls)))
import conexiones.urls as conexiones_urls

# Automatically added app include
urlpatterns.append(path('', include(conexiones_urls)))
import tejidos.urls as tejidos_urls

# Automatically added app include
urlpatterns.append(path('', include(tejidos_urls)))
import usuarios.urls as usuarios_urls

# Automatically added app include
urlpatterns.append(path('', include(usuarios_urls)))
import simulacion.urls as simulacion_urls

# Automatically added app include
urlpatterns.append(path('', include(simulacion_urls)))
import user_management.urls as user_management_urls

# Automatically added app include
urlpatterns.append(path('', include(user_management_urls)))
