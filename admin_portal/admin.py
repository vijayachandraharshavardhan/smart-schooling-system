from django.contrib import admin
from .models import (
    Class, Student, Teacher, Announcement, Homework, Performance,
    AboutInfo, ResultInfo, ContactInfo
)

# ------------------------------
# CLASS MODEL ADMIN
# ------------------------------
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("name", "section")
    search_fields = ("name", "section")
    list_per_page = 20


# ------------------------------
# STUDENT MODEL ADMIN
# ------------------------------
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "roll_number", "class_assigned")
    search_fields = ("name", "roll_number")
    list_filter = ("class_assigned",)
    list_per_page = 20


# ------------------------------
# TEACHER MODEL ADMIN
# ------------------------------
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "subject")
    search_fields = ("name", "subject")
    filter_horizontal = ("classes",)
    list_per_page = 20


# ------------------------------
# ANNOUNCEMENT MODEL ADMIN
# ------------------------------
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "message")
    ordering = ("-created_at",)
    list_per_page = 20


# ------------------------------
# HOMEWORK MODEL ADMIN
# ------------------------------
@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ("title", "due_date", "class_assigned")
    search_fields = ("title", "description")
    list_filter = ("class_assigned", "due_date")
    ordering = ("-due_date",)
    list_per_page = 20


# ------------------------------
# PERFORMANCE MODEL ADMIN
# ------------------------------
@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "marks_obtained", "total_marks", "exam_date")
    search_fields = ("student__name", "subject")
    list_filter = ("subject", "exam_date")
    ordering = ("-exam_date",)
    list_per_page = 20


# ------------------------------
# ABOUT INFO MODEL ADMIN
# ------------------------------
@admin.register(AboutInfo)
class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_at")
    search_fields = ("title", "description")
    readonly_fields = ("updated_at",)
    ordering = ("-updated_at",)
    list_per_page = 20


# ------------------------------
# RESULT INFO MODEL ADMIN
# ------------------------------
@admin.register(ResultInfo)
class ResultInfoAdmin(admin.ModelAdmin):
    list_display = ("exam_name", "year", "uploaded_at")
    search_fields = ("exam_name", "summary")
    readonly_fields = ("uploaded_at",)
    ordering = ("-uploaded_at",)
    list_filter = ("year",)
    list_per_page = 20


# ------------------------------
# CONTACT INFO MODEL ADMIN
# ------------------------------
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("school_name", "email", "phone", "updated_at")
    search_fields = ("school_name", "email", "phone", "address")
    readonly_fields = ("updated_at",)
    ordering = ("-updated_at",)
    list_per_page = 20
