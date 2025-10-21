from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('login/admin/', views.login_admin, name='login_admin'),
    path('login/teacher/', views.login_teacher, name='login_teacher'),
]
