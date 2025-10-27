from django.shortcuts import render
from .models import ContactInfo

def contactus_list(request):
    contact = ContactInfo.objects.last()  # fetch latest contact info
    return render(request, "contactus/list.html", {"contact": contact})
