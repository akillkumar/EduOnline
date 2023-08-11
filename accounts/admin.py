from django.contrib import admin
from .models import Profile, FeedBack


admin.site.register(FeedBack)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['picture','username','address','mobile']
    list_display_links = ['picture','username','address','mobile']



admin.site.site_title = 'EduOnline'
admin.site.index_title = 'EduOnline - Administration'
admin.site.site_header = 'EduOnline'
admin.site.site_url = '/'
admin.site.app_index_template = 'test'