from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    # Authentication
    path('login/', views.teacher_login, name='login'),
    path('logout/', views.teacher_logout, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Attendance
    path('attendance/', views.attendance, name='attendance'),
    path('attendance/<int:class_id>/', views.attendance, name='attendance_by_class'),

    # Homework
    path('homework/', views.homework, name='homework'),

    # Exams
    path('exams/', views.exams, name='exams'),

    # Performance
    path('performance/', views.performance, name='performance'),
]
