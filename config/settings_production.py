import os
import dj_database_url
from pathlib import Path
from .settings import *

# -----------------------------------
# BASE DIR FIX
# -----------------------------------
# Ensure BASE_DIR is defined even when imported from settings
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------
# PRODUCTION SETTINGS
# -----------------------------------

# SECURITY
SECRET_KEY = os.environ.get('SECRET_KEY', 'juybaItHJJr3gt7aHGrfuxwTjWeGVe2g8xCj5M4UhEigAf448FvyE8ZKmYPI-WXHbPW8')  # fallback for safety
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ✅ Add your Render domain & localhost
ALLOWED_HOSTS = [
    'smart-schooling-system.onrender.com',
    '.onrender.com',
    'localhost',
    '127.0.0.1',
]

# -----------------------------------
# DATABASE (PostgreSQL for Render)
# -----------------------------------
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    # ✅ Render PostgreSQL with SSL required
    DATABASES = {
        'default': dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    # fallback for local development
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'smart_schooling',
            'USER': 'smart_schooling_user',
            'PASSWORD': os.environ.get('DB_PASSWORD', '30u9m67dN95DoisgtDLn4bvbBtH7khNy'),
            'HOST': os.environ.get('DB_HOST', 'dpg-d3vpoo49c44c738q3c8g-a.oregon-postgres.render.com'),
            'PORT': os.environ.get('DB_PORT', '5432'),
            'OPTIONS': {'sslmode': 'require'},
        }
    }

# -----------------------------------
# STATIC FILES (Production)
# -----------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

if (BASE_DIR / 'static').exists():
    STATICFILES_DIRS = [BASE_DIR / 'static']

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -----------------------------------
# MEDIA FILES (Cloudinary for Production)
# -----------------------------------
import cloudinary_storage

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # fallback for local

# -----------------------------------
# SECURITY SETTINGS
# -----------------------------------
SECURE_SSL_REDIRECT = True  # Enable SSL redirect for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# -----------------------------------
# ✅ CSRF Trusted Origins (important for Render)
# -----------------------------------
CSRF_TRUSTED_ORIGINS = [
    'https://smart-schooling-system.onrender.com',
    'https://*.onrender.com',
]

# -----------------------------------
# LOGGING
# -----------------------------------
LOG_DIR = BASE_DIR / 'logs'
os.makedirs(LOG_DIR, exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR / 'django.log',
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# -----------------------------------
# AUTO SUPERUSER PASSWORD (optional)
# -----------------------------------
os.environ.setdefault('DJANGO_SUPERUSER_PASSWORD', 'admin123')

# -----------------------------------
# MEDIA STORAGE (Cloudinary)
# -----------------------------------
if os.environ.get("CLOUDINARY_URL"):
    INSTALLED_APPS += ['cloudinary', 'cloudinary_storage']

    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
        'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
        'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
    }

MEDIA_URL = '/media/'
