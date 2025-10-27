from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'name', 'student_class')
    list_filter = ('student_class',)
    search_fields = ('name', 'roll_number')

admin.site.register(Student, StudentAdmin)
