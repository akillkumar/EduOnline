from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),

    path('', include('blog.urls')),

    path('account/', include('accounts.urls')),
    path('staff/', include('staff.urls')),
    path('teacher/',include('teacher.urls')),
    path('student/',include('student.urls')),
    path('quiz/',include('quiz.urls')),
    path('course/',include('course.urls')),
    path('assignment/',include('assignment.urls')),
    path('chat/',include('chat.urls')),
    
]

handler404 = 'accounts.views.error_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)