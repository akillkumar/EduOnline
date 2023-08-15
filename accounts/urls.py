from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, LoginView
urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('after-login', afterLogin, name='after-login'),
    path('register/', registration_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

    path('edit-user/<str:user>', edit_user_data, name='edit_user_data'),
    path('edit-profile/<str:user>', edit_profile, name='edit_profile'),
    path('profile/<str:user>', profile, name='profile'),

    path('feedback/<str:user>/', feedback, name='feedback'),
]