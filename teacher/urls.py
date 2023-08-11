from django.urls import path
from teacher import views

urlpatterns = [
path('', views.teacher_dashboard,name='teacher'),

]