
from django.contrib import admin
from django.urls import path, include

from APP_Login import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('loginout/', views.loginout, name='loginout'),
    path('skip_welcome/', views.skip_welcome, name='skip_welcome'),

]
