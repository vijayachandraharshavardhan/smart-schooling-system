from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ------------------------------
    # Homepage (public site root)
    # ------------------------------
    path("", TemplateView.as_view(template_name="index.html"), name="home"),

    # ------------------------------
    # Django default admin
    # ------------------------------
    path("admin/", admin.site.urls),

    # ------------------------------
    # Core App URLs
    # ------------------------------
    path("attendance/", include(("attendance.urls", "attendance"), namespace="attendance")),
    path("exams/", include(("exams.urls", "exams"), namespace="exams")),
    path("notifications/", include(("notifications.urls", "notifications"), namespace="notifications")),
    path("announcements/", include(("announcements.urls", "announcements"), namespace="announcements")),
    path("performance/", include(("performance.urls", "performance"), namespace="performance")),

    # ------------------------------
    # Role-based dashboards
    # ------------------------------
    path("student/", include(("student.urls", "student"), namespace="student")),
    path("teacher/", include(("teacher.urls", "teacher"), namespace="teacher")),  # teacher URLs include logout
    path("achievements/", include(("achievements.urls", "achievements"), namespace="achievements")),
    path("users/", include(("users.urls", "users"), namespace="users")),

    # ------------------------------
    # Custom Admin Portal
    # ------------------------------
    path("admin_portal/", include(("admin_portal.urls", "admin_portal"), namespace="admin_portal")),

    # ------------------------------
    # Other Dynamic Sections
    # ------------------------------
    path("aboutus/", include(("aboutus.urls", "aboutus"), namespace="aboutus")),
    path("ranks/", include(("ranks.urls", "ranks"), namespace="ranks")),
    path("contactus/", include(("contactus.urls", "contactus"), namespace="contactus")),
    path("", include(("school.urls", "school"), namespace="school")),  # fallback school app
]

# ------------------------------
# Static + Media files (development only)
# ------------------------------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
