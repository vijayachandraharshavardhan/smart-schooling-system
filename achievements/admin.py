from django.contrib import admin
from .models import Achievement

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("title", "description")
