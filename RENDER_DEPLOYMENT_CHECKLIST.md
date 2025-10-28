# Render Deployment Checklist

## Pre-Deployment Steps
- [x] Update `render.yaml` with correct service configuration
- [x] Ensure `requirements_production.txt` has all necessary dependencies
- [x] Configure production settings in `config/settings_production.py`
- [x] Set up database configuration for PostgreSQL
- [x] Configure static files handling with WhiteNoise
- [x] Set up health check endpoint
- [x] Test application locally with production settings
- [x] Verify all URLs are working correctly
- [x] Run `python manage.py check --deploy` and fix warnings

## Deployment Steps
1. Push code to GitHub repository
2. Connect Render account to GitHub
3. Create new Web Service on Render
4. Configure build and start commands:
   - Build Command: `pip install -r requirements_production.txt`
   - Start Command: `python manage.py migrate && python manage.py createsuperuser --noinput --username Harsha@108 --email harsha@school.com || true && python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`
5. Add PostgreSQL database in Render dashboard
6. Set environment variables:
   - `DJANGO_SETTINGS_MODULE=config.settings_production`
   - `SECRET_KEY` (generate a secure key)
   - `DATABASE_URL` (provided by Render PostgreSQL)
   - `DJANGO_SUPERUSER_PASSWORD=admin123`
7. Deploy the application

## Post-Deployment Verification
- [x] Health check endpoint returns 200: `/health/`
- [x] Home page loads correctly: `/`
- [x] Admin login works: `/admin/`
- [x] User login pages work: `/users/login/teacher/`
- [x] Dashboard pages accessible: `/student/`, `/teacher/dashboard/`
- [x] Static files are served correctly
- [x] Database migrations applied successfully
- [x] Superuser account created
- [x] School profile data seeded

## Known Issues and Notes
- SECURE_SSL_REDIRECT is set to False (Render handles SSL)
- Template naming conflict warning (student_filters used in multiple modules)
- Database falls back to SQLite if DATABASE_URL not set (for local testing)

## Environment Variables Required
- `DATABASE_URL`: PostgreSQL connection string from Render
- `SECRET_KEY`: Django secret key (auto-generated if not set)
- `DJANGO_SETTINGS_MODULE`: config.settings_production
- `DJANGO_SUPERUSER_PASSWORD`: admin123

## Troubleshooting
- If deployment fails, check Render logs for specific errors
- Ensure all dependencies are in requirements_production.txt
- Verify database connection string format
- Check that static files are collected properly
