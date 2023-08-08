"""
URL configuration for project16 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
    path('first/',first,name='first'),
    path('second/',second,name='second'),
    path('farmer/',farmer,name='farmer'),
    path('farmer_lg/',farmer_lg,name='farmer_lg'),
    path('farmer_Resisation/',farmer_Resisation,name='farmer_Resisation'),
    path('java_jam/',java_jam,name='java_jam'),
    path('Happy_born/',Happy_born,name='Happy_born'),
    path('jspiders/',jspiders,name='jspiders'),
    path('onlineform/',onlineform,name='onlineform'),
    path('facebook/',facebook,name='facebook'),
    path('margin/',margin,name='margin'),
    path('transfermation/',transfermation,name='transfermation'),
    path('nasted_table/',nasted_table,name='nasted_table'),
    path('tablein/',tablein,name='tablein'),
    path('km_custom/',km_custom,name='km_custom'),
    
]
