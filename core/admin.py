from django.contrib import admin
from .models import School, Course


# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("school_name", "location")

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name", "school")


admin.site.register(School, SchoolAdmin)
admin.site.register(Course, CourseAdmin)
