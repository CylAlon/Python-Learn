
from django.contrib import admin
from django.urls import path, include

from APP_Statement import views

urlpatterns = [
    path('skip_person/', views.skip_person, name='skip_person'),
    path('show_allkq/', views.show_allkq, name='show_allkq'),
    path('show_cour/', views.show_cour, name='show_cour'),
    path('show_week/', views.show_week, name='show_week'),
    path('show_day/', views.show_day, name='show_day'),
    path('show_num/', views.show_num, name='show_num'),
    path('show_state/', views.show_state, name='show_state'),
    path('show_page/', views.show_page, name='show_page'),
    path('show_print/', views.show_print, name='show_print'),


    path('skip_class/', views.skip_class, name='skip_class'),
    path('show_allcl/', views.show_allcl, name='show_allcl'),
    path('show_court/', views.show_court, name='show_court'),
    path('show_stut/', views.show_stut, name='show_stut'),
    path('show_weekt/', views.show_weekt, name='show_weekt'),
    path('show_dayt/', views.show_dayt, name='show_dayt'),
    path('show_numt/', views.show_numt, name='show_numt'),
    path('show_statet/', views.show_statet, name='show_statet'),
    path('show_paget/', views.show_paget, name='show_paget'),
    path('show_printt/', views.show_printt, name='show_printt'),




]
