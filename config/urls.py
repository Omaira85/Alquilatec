"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from alquilatec.views import index, equipos, principal, contacto, \
        registro, guardar_usuario, acceder, salir, \
        consultar_equipos, alquilar


urlpatterns = [
    path('', index),
    path('equipos', equipos),
    path('alquilar', alquilar),
    path('consultar-equipos', consultar_equipos),
    path('contacto', contacto),
    path('principal', principal),
    path('registro', registro),
    path('guardar-usuario', guardar_usuario),
    path('login', acceder),
    path('logout', salir),
    path('admin/', admin.site.urls),
]
