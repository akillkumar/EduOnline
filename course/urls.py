from django.urls import path
from . import views


urlpatterns = [
    path('', views.courses, name='courses'),
    path('my-courses/', views.myCourses, name='myCourses'),
    path('<courseName>/', views.details, name='courseDetails'),
    path('enroll/<str:course_name>/', views.enroll, name='enroll'),
    path('<courseName>/<int:videoId>/', views.watchCourse, name='watchCourse'),
    
    path('my-courses/<str:course_name>/', views.course_page, name='course_page'),
    path('courses-management', views.management, name='course-manage'),
    path('edit-courses/<course_id>', views.edit_course, name='edit-course'),
    path('add-video/<course_id>', views.upload_videos, name='upload-video'),


    path('create/<course_name>', views.create_course_videos_from_file, name='create_course_videos'),
]