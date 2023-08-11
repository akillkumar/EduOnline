from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)