from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = "student"

urlpatterns = [
    # Redirect /student/ → dashboard
    path('', lambda request: redirect('student:dashboard'), name='home'),

    # Main dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Student sections
    path('attendance/', views.attendance_view, name='attendance'),
    path('homework/', views.homework_view, name='homework'),
    path('exams/', views.exams_view, name='exams'),
    path('performance/', views.performance_view, name='performance'),
]
