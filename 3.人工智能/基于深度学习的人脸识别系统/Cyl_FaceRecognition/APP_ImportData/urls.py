
from django.contrib import admin
from django.urls import path, include

from APP_ImportData import views

urlpatterns = [
    path('skip_import/', views.skip_import, name='skip_import'),
    path('face_gather/', views.face_gather, name='face_gather'),
    path('student_info/', views.student_info, name='student_info'),
    path('teacher_info/', views.teacher_info, name='teacher_info'),
    path('admin_info/', views.admin_info, name='admin_info'),
    path('class_info/', views.class_info, name='class_info'),
    path('course_info/', views.course_info, name='course_info'),
    path('course_table/', views.course_table, name='course_table'),
    path('college_info/', views.college_info, name='college_info'),
    path('specialty_info/', views.specialty_info, name='specialty_info'),

    # 以下是人脸数据采集
    path('class_info_face/', views.class_info_face, name='class_info_face'),
    path('cloose_stu/', views.cloose_stu, name='cloose_stu'),
    path('fenye/', views.fenye, name='fenye'),

]
