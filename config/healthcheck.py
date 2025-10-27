"""
Simple healthcheck view for Railway deployment
"""
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import os

@csrf_exempt
@require_http_methods(["GET"])
def healthcheck(request):
    """
    Simple healthcheck endpoint that returns basic system info
    """
    try:
        # Basic system info
        info = {
            "status": "healthy",
            "message": "Smart Schooling System is running",
            "environment": {
                "DEBUG": os.environ.get('DEBUG', 'Not set'),
                "DJANGO_SETTINGS_MODULE": os.environ.get('DJANGO_SETTINGS_MODULE', 'Not set'),
                "RAILWAY_ENVIRONMENT": os.environ.get('RAILWAY_ENVIRONMENT', 'Not set'),
                "SECRET_KEY_SET": "Yes" if os.environ.get('SECRET_KEY') else "No",
                "DATABASE_URL_SET": "Yes" if os.environ.get('DATABASE_URL') else "No",
            }
        }
        return JsonResponse(info, status=200)
    except Exception as e:
        return JsonResponse({
            "status": "unhealthy",
            "error": str(e)
        }, status=500)
