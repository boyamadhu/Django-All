"""Logins URL Configuration

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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Login_Form/',Login_Form,name='Login_Form'),
    path('Reister_Form/',Reister_Form,name='Reister_Form'),
    path('Data_Student/',Data_Student,name='Data_Student'),
    path('Retrieve_Data/',Retrieve_Data,name='Retrieve_Data'),
    path('Data_table/',Data_table,name='Data_table'),
]
