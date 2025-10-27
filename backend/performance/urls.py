from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='performance/analytics.html')),
    path('leaderboard/', TemplateView.as_view(template_name='performance/leaderboard.html')),
]
