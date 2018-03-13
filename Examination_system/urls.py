"""Examination_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from homepage import views as homepage
from homepage import time as time

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('verification',homepage.verification),
    path('',homepage.login,name="login"),
    path('create_code/',homepage.create_code_img,name="yanzhengma"),
    path('index.html',homepage.indexpage,name="dengluchenggong"),
    path('exit.html',homepage.exit_login,name="exit"),
    path('curriculum',homepage.curriculum),
    path('examination',homepage.examination),
    path('Subject',homepage.subject),
    path('Examination',homepage.Examination),
    path('Judge',homepage.Judge),
    path('achievement/finish',homepage.last_achievement),
    path('record',homepage.show_historical_achievement),
    path('PersonalInformation',homepage.PersonalInformation),
    #path('jishiqi.html',time.time),
]
