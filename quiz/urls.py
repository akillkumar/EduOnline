from django.urls import path
from . import views

urlpatterns = [
    path('', views.available_quizzes, name='available_quizzes'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/calculate_score/', views.calculate_score, name='calculate_score'),

    path('add-quiz/', views.add_quiz, name='add_quiz'),
    path('add-question/', views.add_questions, name='add_questions'),
    path('add-option/', views.add_options, name='add_options'),

    path('remove-quiz/<int:quiz_id>/', views.remove_quiz, name='remove_quiz'),
    path('edit-quiz/<int:quiz_id>/', views.edit_quiz, name='edit_quiz'),

    path('student-results/', views.results_page, name='results_page'),
    path('<str:student>/result/', views.result, name='result'),
]
