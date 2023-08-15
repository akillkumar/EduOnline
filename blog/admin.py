from django.contrib import admin
from .models import *


admin.site.register(Book)
admin.site.register(Article)


@admin.register(ContactUs)
class Contact(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'email', 'message']