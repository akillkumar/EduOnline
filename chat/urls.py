from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='inbox'),
    path('chat/<int:user_id>/', views.chat, name='chat'),
    path('send-message/<int:user_id>/', views.send_message, name='send-message'),
]
