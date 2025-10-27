from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='exams/schedule.html')),
    path('results/', TemplateView.as_view(template_name='exams/results.html')),
]
