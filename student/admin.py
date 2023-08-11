from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user',"profile_pic"]
    list_display_links = ['user',"profile_pic"]