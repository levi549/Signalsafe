"""
URL configuration for API_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from API.views import cadastro, login, get_estabelecimento,get_sala,get_jammer,create_estabelecimento,create_sala,create_jammer,update_jammer
from django.http import HttpResponse
def bem_vindo(request):
    return HttpResponse("servidor funcionando")
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('auth/cadastro/', cadastro,name='cadastro'),
    path('auth/login/', login,name='login'),
    path('',bem_vindo,name='bem vindo'),
    path('get/estabelecimento',get_estabelecimento,name='get_estabelecimento'),
    path('get/sala/',get_sala,name='get_sala'),
    path('get/jammer',get_jammer,name='get_jammer'),
    path('update/jammer ',update_jammer,name='update_jammer')
]
