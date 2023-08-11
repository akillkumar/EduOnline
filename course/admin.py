from django.contrib import admin
from .models import *


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name','description','field','image']


admin.site.register(CourseVideos)
admin.site.register(Enrolled)
# admin.site.register(AssignmentTeacher)
# admin.site.register(AssignmentStudent)