from django.urls import path
from . import views

urlpatterns = [
    path('', views.assignment_list, name='assignment'),
    path('result/<str:user>/', views.results, name='assignment_result'),
    path('add-assignment/', views.add_assignment, name='add-assignment'),
    path('upload-assignment/<int:assignment_id>/', views.student_upload_assignment, name='upload-assignment'),
    path('review-assignment/<int:assignmentId>/', views.teacher_review_assignment, name='review-assignment'),
    path('edit_assignment/<int:assignment_id>/', views.edit_assignment, name='edit-assignment'),    
    path('delete_assignment/<int:assignment_id>/', views.delete_assignment, name='delete-assignment'),

    path('review_assignment/', views.review_assignment, name='review_assignment'),
]
