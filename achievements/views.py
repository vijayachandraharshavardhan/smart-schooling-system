from django.shortcuts import render, get_object_or_404
from .models import Achievement

def achievements_view(request):
    professional_achievements = Achievement.objects.filter(category='professional').order_by('-highlight', '-id')
    sports_achievements = Achievement.objects.filter(category='sports').order_by('-highlight', '-id')
    return render(request, 'achievements/achievements.html', {
        'professional_achievements': professional_achievements,
        'sports_achievements': sports_achievements
    })


def achievement_detail(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    return render(request, 'achievements/achievement_detail.html', {
        'achievement': achievement
    })
