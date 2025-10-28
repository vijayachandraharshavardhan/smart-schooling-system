# import os
# from pathlib import Path

# # -----------------------------------
# # BASE DIRECTORY
# # -----------------------------------
# BASE_DIR = Path(__file__).resolve().parent.parent

# # -----------------------------------
# # SECURITY
# # -----------------------------------
# SECRET_KEY = "replace-this-with-a-strong-key"
# DEBUG = True
# ALLOWED_HOSTS = []  # ["127.0.0.1", "localhost"]

# # Production settings override
# import os
# if os.environ.get('RAILWAY_ENVIRONMENT') or os.environ.get('HEROKU_APP_NAME'):
#     from .settings_production import *

# # -----------------------------------
# # INSTALLED APPS
# # -----------------------------------
# INSTALLED_APPS = [
#     # Django default apps
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",

#     # Project apps
#     "users",
#     "admin_portal",
#     "teacher",
#     "student",
#     "achievements",
#     "attendance",
#     "exams",
#     "performance",
#     "notifications",
#     "announcements",
#     "aboutus",
#     "contactus",
#     "ranks",
#     "school",


# ]

# # -----------------------------------
# # MIDDLEWARE
# # -----------------------------------
# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]

# # -----------------------------------
# # URLS + WSGI
# # -----------------------------------
# ROOT_URLCONF = "config.urls"
# WSGI_APPLICATION = "config.wsgi.application"

# # -----------------------------------
# # TEMPLATES
# # -----------------------------------
# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         # Global templates folder (optional)
#         "DIRS": [BASE_DIR / "templates"],
#         "APP_DIRS": True,  # automatically looks inside app_name/templates/
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]
# # Allow your deployed domain to make POST requests
# CSRF_TRUSTED_ORIGINS = [
#     "https://smart-schooling-system-production.up.railway.app",
# ]

# # Allow your deployed domain to access your app
# ALLOWED_HOSTS = [
#     "smart-schooling-system-production.up.railway.app",
#     "127.0.0.1",
#     "localhost",
# ]


# # -----------------------------------
# # DATABASE (SQLite)
# # -----------------------------------
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# # -----------------------------------
# # STATIC FILES
# # -----------------------------------
# STATIC_URL = "/static/"
# STATICFILES_DIRS = [BASE_DIR / "static"]  # project-level static
# STATIC_ROOT = BASE_DIR / "staticfiles"

# # -----------------------------------
# # MEDIA FILES
# # -----------------------------------
# MEDIA_URL = "/media/"
# MEDIA_ROOT = BASE_DIR / "media"

# # -----------------------------------
# # AUTHENTICATION SETTINGS
# # -----------------------------------
# # Teacher login paths
# LOGIN_URL = "/users/login/teacher/"
# LOGIN_REDIRECT_URL = "/teacher/dashboard/"
# LOGOUT_REDIRECT_URL = "/users/login/teacher/"

# # -----------------------------------
# # DEFAULT PRIMARY KEY FIELD TYPE
# # -----------------------------------
# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# # -----------------------------------
# # SESSION SETTINGS
# # -----------------------------------
# SESSION_COOKIE_AGE = 60 * 60 * 8  # 8 hours
# SESSION_SAVE_EVERY_REQUEST = True


import os
from pathlib import Path

# -----------------------------------
# BASE DIRECTORY
# -----------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------
# SECURITY
# -----------------------------------
SECRET_KEY = "replace-this-with-a-strong-key"

# Set DEBUG = False in production for safety
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

# -----------------------------------
# ALLOWED HOSTS & CSRF
# -----------------------------------
ALLOWED_HOSTS = [
    "smart-schooling-system-production.up.railway.app",
    "127.0.0.1",
    "localhost",
]

# ✅ Allow POST requests from Railway domain (important for CSRF)
CSRF_TRUSTED_ORIGINS = [
    "https://smart-schooling-system-production.up.railway.app",
]

# ✅ Secure cookies when using HTTPS (Railway uses HTTPS)
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# ✅ Optional: allow same-site cookies (needed for embedded dashboards)
CSRF_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SAMESITE = "Lax"

# -----------------------------------
# PRODUCTION SETTINGS OVERRIDE
# -----------------------------------
if os.environ.get('RAILWAY_ENVIRONMENT') or os.environ.get('HEROKU_APP_NAME') or os.environ.get('RENDER'):
    from .settings_production import *

# -----------------------------------
# INSTALLED APPS
# -----------------------------------
INSTALLED_APPS = [
    # Django default apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Project apps
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

# -----------------------------------
# MIDDLEWARE
# -----------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# -----------------------------------
# URLS + WSGI
# -----------------------------------
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# -----------------------------------
# TEMPLATES
# -----------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

# -----------------------------------
# DATABASE (SQLite for now)
# -----------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# -----------------------------------
# STATIC FILES
# -----------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# -----------------------------------
# MEDIA FILES
# -----------------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# -----------------------------------
# AUTHENTICATION SETTINGS
# -----------------------------------
LOGIN_URL = "/users/login/teacher/"
LOGIN_REDIRECT_URL = "/teacher/dashboard/"
LOGOUT_REDIRECT_URL = "/users/login/teacher/"

# -----------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# -----------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -----------------------------------
# SESSION SETTINGS
# -----------------------------------
SESSION_COOKIE_AGE = 60 * 60 * 8  # 8 hours
SESSION_SAVE_EVERY_REQUEST = True
