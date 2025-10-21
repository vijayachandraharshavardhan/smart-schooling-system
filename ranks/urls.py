from django.urls import path
from . import views

app_name = 'ranks'

urlpatterns = [
    path('', views.rank_list, name='list'),
]
