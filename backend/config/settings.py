import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# ------------------------------------------------------
# BASE SETTINGS
# ------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env (for local dev)
load_dotenv()

# ------------------------------------------------------
# SECURITY
# ------------------------------------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "P2TSKAMghkuvqdr6xt-WJdap6J9lrLZXOB0cRVmafKxMatH1FP2IsR5FlqY_RmbQypM")
DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS = ["*"]  # For Render; you can restrict later

# Production security settings
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# ------------------------------------------------------
# INSTALLED APPS
# ------------------------------------------------------
INSTALLED_APPS = [
    # Django default apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Your project apps
    "users",
    "admin_portal",
    "teacher",
    "student",
    "achievements",
    "attendance",
    "exams",
    "performance",
    "notifications",
    "announcements",
    "aboutus",
    "contactus",
    "ranks",
    "school",
]

# ------------------------------------------------------
# MIDDLEWARE
# ------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # <-- Added for Render static files
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ------------------------------------------------------
# URLS + WSGI
# ------------------------------------------------------
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# ------------------------------------------------------
# TEMPLATES
# ------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # global templates folder
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ------------------------------------------------------
# DATABASE (works both locally & on Render)
# ------------------------------------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv(
            "DATABASE_URL",
            "postgresql://postgres:Harsha@108@localhost:5432/deeptihome"
        ),
        conn_max_age=600,
    )
}

# ------------------------------------------------------
# STATIC & MEDIA FILES
# ------------------------------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ------------------------------------------------------
# AUTHENTICATION SETTINGS
# ------------------------------------------------------
LOGIN_URL = "/users/login/teacher/"
LOGIN_REDIRECT_URL = "/teacher/dashboard/"
LOGOUT_REDIRECT_URL = "/users/login/teacher/"

# ------------------------------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# ------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ------------------------------------------------------
# SESSION SETTINGS
# ------------------------------------------------------
SESSION_COOKIE_AGE = 60 * 60 * 8  # 8 hours
SESSION_SAVE_EVERY_REQUEST = True
