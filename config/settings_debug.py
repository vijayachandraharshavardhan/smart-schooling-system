import os
from pathlib import Path

# -----------------------------------
# BASE DIRECTORY
# -----------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------
# SECURITY
# -----------------------------------
SECRET_KEY = os.environ.get('SECRET_KEY', 'debug-key-for-railway-testing')
DEBUG = True  # Keep debug on for now to see errors
ALLOWED_HOSTS = ['*']  # Allow all hosts for debugging

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
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Add WhiteNoise
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
# DATABASE (SQLite for debugging)
# -----------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Try PostgreSQL if available
if 'DATABASE_URL' in os.environ:
    try:
        import dj_database_url
        DATABASES['default'] = dj_database_url.parse(os.environ['DATABASE_URL'])
    except ImportError:
        pass  # Use SQLite if dj_database_url not available

# -----------------------------------
# STATIC FILES
# -----------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Use WhiteNoise for static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

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

# -----------------------------------
# LOGGING (for debugging)
# -----------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
