
from django.contrib import admin
from django.urls import path, include

from APP_Check import views

urlpatterns = [
    path('skip_check/', views.skip_check, name='skip_check'),
    path('skip_set_check/', views.skip_set_check, name='skip_set_check'),
    path('set_check/', views.set_check, name='set_check'),


    path('show_college/', views.show_college, name='show_college'),
    path('show_week/', views.show_week, name='show_week'),
    path('show_day/', views.show_day, name='show_day'),
    path('show_num/', views.show_num, name='show_num'),
    path('show_conf/', views.show_conf, name='show_conf'),
    path('show_kaoqin/', views.show_kaoqin, name='show_kaoqin'),
    path('show_pagetrun/', views.show_pagetrun, name='show_pagetrun'),
    path('show_deta/', views.show_deta, name='show_deta'),
    path('show_gb/', views.show_gb, name='show_gb'),
    path('show_xq/', views.show_xq, name='show_xq'),




    # path('show_page/', views.show_page, name='show_page'),

]
