"""boostrap_django_Project URL Configuration

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
from boostrap_django_Project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='myindex'),
    path('about/', views.about, name='myabout'),
    path('blog/', views.blog, name='myblog'),
    path('class/', views.classes, name='myclass'),
    path('contact/', views.contact, name='mycontact'),
    path('detail/', views.detail, name='mydetail'),
    path('trainers/', views.team, name='myteam'),
    path('testimony/', views.testimony, name='mytestimonial')


]
