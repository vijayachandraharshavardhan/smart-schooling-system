# achievements/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.achievements_view, name='achievements'),
    path('<int:pk>/', views.achievement_detail, name='achievement_detail'),
]
