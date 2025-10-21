# Smart Schooling System

Django-based school management system for DEEPTI EM HIGH SCHOOL.

## Features
- Student Management
- Teacher Portal
- Admin Dashboard
- Attendance Tracking
- Performance Monitoring
- Exam Management
- Announcements
- Achievements Showcase

## Technology Stack
- Django 4.2+
- PostgreSQL
- Bootstrap 5
- Python 3.9+

## Deployment
This project is configured for Railway deployment with:
- Production-ready settings
- PostgreSQL database
- Static file serving
- Security configurations

## Quick Start
1. Install dependencies: `pip install -r requirements_production.txt`
2. Run migrations: `python manage.py migrate`
3. Create superuser: `python manage.py createsuperuser`
4. Collect static files: `python manage.py collectstatic --noinput`
5. Start server: `gunicorn config.wsgi:application`

## Environment Variables
- `SECRET_KEY`: Django secret key
- `DJANGO_SETTINGS_MODULE`: config.settings_production
- `RAILWAY_ENVIRONMENT`: production
- `DEBUG`: False

## Author
Developed by B.V.C. Harsha Vardhan
