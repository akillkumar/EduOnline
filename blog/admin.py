from django.contrib import admin
from .models import *


admin.site.register(Book)


@admin.register(ContactUs)
class Contact(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'email', 'message']