from django.shortcuts import render
from .models import AboutUs

def aboutus_list(request):
    # Fetch all AboutUs entries ordered by latest update
    about_entries = AboutUs.objects.all().order_by('-updated_at')
    return render(request, 'aboutus/list.html', {'about_entries': about_entries})
