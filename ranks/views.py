from django.shortcuts import render
from .models import Rank

def rank_list(request):
    ranks = Rank.objects.all().order_by('position')
    return render(request, 'ranks/list.html', {'ranks': ranks})
