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
    '*.onrender.com', # Render domains
    '*.herokuapp.com', # Heroku domains
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
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

# CSRF Trusted Origins for Heroku - Comprehensive configuration
CSRF_TRUSTED_ORIGINS = [
    'https://smart-schooling-system.herokuapp.com',
    'https://smart-schooling-system.herokuapp.com/',
    'https://*.herokuapp.com',
    'https://*.herokuapp.com/',
    # Keep Railway origins as fallback
    'https://smart-schooling-system-production.up.railway.app',
    'https://smart-schooling-system-production.up.railway.app/',
    'https://*.railway.app',
    'https://*.railway.app/',
    # Keep Render origins as fallback
    'https://smart-schooling-system.onrender.com',
    'https://smart-schooling-system.onrender.com/',
    'https://*.onrender.com',
    'https://*.onrender.com/',
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

# Set default password for auto-created superuser
os.environ.setdefault('DJANGO_SUPERUSER_PASSWORD', 'admin123')

# Temporary database debugging - remove after fixing
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("=== DATABASE CONFIGURATION DEBUG ===")
logger.info(f"PGHOST: {os.environ.get('PGHOST', 'NOT SET')}")
logger.info(f"PGPORT: {os.environ.get('PGPORT', 'NOT SET')}")
logger.info(f"PGDATABASE: {os.environ.get('PGDATABASE', 'NOT SET')}")
logger.info(f"PGUSER: {os.environ.get('PGUSER', 'NOT SET')}")
logger.info(f"PGPASSWORD: {'SET' if os.environ.get('PGPASSWORD') else 'NOT SET'}")
logger.info(f"DATABASE_URL: {os.environ.get('DATABASE_URL', 'NOT SET')}")
logger.info(f"Final DATABASES config: {DATABASES['default']}")
logger.info("=== END DATABASE DEBUG ===")
