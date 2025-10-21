import os
from pathlib import Path
from .settings import *

# -----------------------------------
# PRODUCTION SETTINGS
# -----------------------------------

# SECURITY
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-super-secret-key-here-change-this')
DEBUG = False
ALLOWED_HOSTS = [
    '*.railway.app',  # Railway domains
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
    '.herokuapp.com',  # Heroku domains
    '.vercel.app',     # Vercel domains
    '.netlify.app',    # Netlify domains
]

# -----------------------------------
# DATABASE (PostgreSQL for production)
# -----------------------------------
# Database configuration for Railway
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PGDATABASE', 'railway'),
        'USER': os.environ.get('PGUSER', 'postgres'),
        'PASSWORD': os.environ.get('PGPASSWORD', ''),
        'HOST': os.environ.get('PGHOST', 'containers-us-west-1.railway.app'),  # Railway default
        'PORT': os.environ.get('PGPORT', '5432'),
        'OPTIONS': {
            'sslmode': 'require',  # Railway requires SSL
        },
    }
}

# Fallback to DATABASE_URL if individual variables are not set
if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES['default'] = dj_database_url.parse(os.environ['DATABASE_URL'])
else:
    # Alternative Railway database URL construction
    if all(key in os.environ for key in ['PGHOST', 'PGPORT', 'PGDATABASE', 'PGUSER', 'PGPASSWORD']):
        DATABASES['default'] = {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['PGDATABASE'],
            'USER': os.environ['PGUSER'],
            'PASSWORD': os.environ['PGPASSWORD'],
            'HOST': os.environ['PGHOST'],
            'PORT': os.environ['PGPORT'],
            'OPTIONS': {
                'sslmode': 'require',
            },
        }

# -----------------------------------
# STATIC FILES (Production)
# -----------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Use WhiteNoise for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -----------------------------------
# MEDIA FILES (Production)
# -----------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# For production, consider using cloud storage (AWS S3, etc.)
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# -----------------------------------
# SECURITY SETTINGS
# -----------------------------------
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# CSRF Trusted Origins for Railway - Comprehensive list
CSRF_TRUSTED_ORIGINS = [
    'https://smart-schooling-system-production.up.railway.app',
    'https://*.railway.app',
    'http://smart-schooling-system-production.up.railway.app',
    'http://*.railway.app',
    'https://smart-schooling-system-production.railway.app',
    'http://smart-schooling-system-production.railway.app',
    'https://railway.app',
    'http://railway.app',
]

# -----------------------------------
# LOGGING
# -----------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# Create logs directory if it doesn't exist
os.makedirs(BASE_DIR / 'logs', exist_ok=True)
