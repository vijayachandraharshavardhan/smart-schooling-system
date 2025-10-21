from django.urls import path
from django.views.generic import TemplateView
from . import views   # ✅ so we can use home_view, about_view, results_view, contact_view

app_name = "admin_portal"

urlpatterns = [
    # -------- Admin Pages --------
    path('', TemplateView.as_view(template_name='admin_portal/dashboard.html'), name="dashboard"),
    path('manage-users/', TemplateView.as_view(template_name='admin_portal/manage_users.html'), name="manage_users"),
    path('manage-classes/', TemplateView.as_view(template_name='admin_portal/manage_classes.html'), name="manage_classes"),
    path('reports/', TemplateView.as_view(template_name='admin_portal/reports.html'), name="reports"),
    path('school-profile/', TemplateView.as_view(template_name='admin_portal/school_profile.html'), name="school_profile"),

    # -------- Public Site --------
    path('home/', views.home_view, name="home"),           # ✅ renders home.html
    path('about/', views.about_view, name="about"),        # ✅ renders about.html
    path('rankers/', views.results_view, name="rankers"),  # ✅ renders results.html
    path('contact/', views.contact_view, name="contact"),  # ✅ renders contact.html
]
