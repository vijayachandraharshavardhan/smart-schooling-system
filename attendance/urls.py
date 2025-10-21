# attendance/urls.py
from student import views as student_views  # <-- import from student app
from django.urls import path

urlpatterns = [
    path('student/<str:roll_no>/', student_views.attendance_view, name='student_attendance'),
]
