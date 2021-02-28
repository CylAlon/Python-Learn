"""Cyl_FaceRecognition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.myurls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.myurls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_login/', include(('APP_Login.urls', 'APP_Login'), namespace='app_login')),
    path('app_import/', include(('APP_ImportData.urls', 'APP_ImportData'), namespace='app_import')),
    path('app_check/', include(('APP_Check.urls', 'APP_Check'), namespace='app_check')),
    path('app_basic/', include(('APP_BasicInfo.urls', 'APP_BasicInfo'), namespace='app_basic')),
    path('app_statement/', include(('APP_Statement.urls', 'APP_Statement'), namespace='app_statement')),

]
