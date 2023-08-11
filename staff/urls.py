from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [    
    path('dashboard', views.dashboard, name='staff-dashboard'),

    path('staff-teacher', views.staff_teacher,name='staff-teacher'),

    path('staff-view-teacher', views.staff_teacher,name='staff-view-teacher'),
    path('update-teacher/<int:pk>', views.update_teacher,name='update-teacher'),
    path('delete-teacher/<int:pk>', views.delete_teacher,name='delete-teacher'),
    path('staff-view-pending-teacher', views.staff_pending_teacher,name='staff-view-pending-teacher'),
    path('staff-view-teacher-salary', views.staff_teacher_salary,name='staff-view-teacher-salary'),
    path('approve-teacher/<int:pk>', views.approve_teacher,name='approve-teacher'),
    path('reject-teacher/<int:pk>', views.reject_teacher,name='reject-teacher'),

    path('staff-student', views.staff_student,name='staff-student'),
    path('staff-view-student', views.staff_student,name='staff-view-student'),
    path('update-student/<int:pk>', views.update_student,name='update-student'),
    path('delete-student/<int:pk>', views.delete_student,name='delete-student'),

    path('staff-course', views.staff_course,name='staff-course'),
    path('staff-add-course', views.addCourse,name='add-course'),
    path('staff-view-course', views.staff_course,name='staff-view-course'),
    path('delete-course/<int:pk>', views.delete_course,name='delete-course'),


]