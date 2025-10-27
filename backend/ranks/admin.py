from django.contrib import admin
from .models import Rank

@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ('position', 'student_name', 'marks', 'updated_at')
