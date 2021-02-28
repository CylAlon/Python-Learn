
from django.contrib import admin
from django.urls import path, include

from APP_BasicInfo import views

urlpatterns = [
    path('clear_session/', views.clear_session, name='clear_session'),
    path('show_stud/', views.show_stud, name='show_stud'),
    path('show_tb1/', views.show_tb1, name='show_tb1'),

    path('show_ted/', views.show_ted, name='show_ted'),
    path('show_te_std/', views.show_te_std, name='show_te_std'),
    path('show_tecour/', views.show_tecour, name='show_tecour'),


    path('show_set/', views.show_set, name='show_set'),
    path('show_setqr/', views.show_setqr, name='show_setqr'),




]
