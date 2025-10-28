#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Setup Django
django.setup()

from school.views import home
from django.test import RequestFactory

# Create a request factory
rf = RequestFactory()
request = rf.get('/')

# Call the home view
response = home(request)

# Print response details
print('Response status:', response.status_code)
print('Content length:', len(response.content))

# Decode content
content = response.content.decode('utf-8')

# Check if logo is in HTML
print('Logo in HTML:', '/media/logos/SIVA.jpg' in content)

# Find navbar brand section
lines = content.split('\n')
print('Navbar brand section:')
for line in lines:
    if 'navbar-brand' in line:
        print(line.strip())
        break
