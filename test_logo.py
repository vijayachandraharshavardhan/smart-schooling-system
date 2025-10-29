import os
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from school.models import SchoolProfile

profile = SchoolProfile.objects.first()
print('Profile exists:', profile is not None)
if profile:
    print('Logo field:', profile.logo)
    print('Logo URL:', profile.logo.url if profile.logo else 'No logo')
    print('Logo path:', profile.logo.path if profile.logo else 'No path')
else:
    print('No profile found')
