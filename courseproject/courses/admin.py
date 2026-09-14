from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_code', 'duration', 'fee')
    search_fields = ('course_name', 'course_code')
