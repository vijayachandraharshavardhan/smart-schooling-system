from django.contrib import admin
from .models import ContactInfo

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = (
        "principal_name",
        "principal_mobile",
        "correspondent_name",
        "correspondent_mobile",
        "updated_at",
    )
    search_fields = ("principal_name", "correspondent_name", "principal_mobile", "correspondent_mobile")
