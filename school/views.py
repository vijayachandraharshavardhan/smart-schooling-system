from django.shortcuts import render
from school.models import SchoolProfile

def home(request):
    profile = SchoolProfile.objects.first()  # only one profile (school)
    return render(request, 'index.html', {'profile': profile})
