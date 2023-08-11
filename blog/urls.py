from django.urls import path
from . import views


urlpatterns = [
  path('',views.home,name='home'),
  path('about-us', views.aboutUs, name='aboutUs'),
  path('contact-us', views.contactUs, name='contactUs'),


  path('blog/', views.blog, name='blog'),
  path('blog/article/<ID>', views.article, name='article'),
  
  path('blog/add-article', views.addArticle, name='addArticle' ),
  path('library/', views.library, name='library'),
  path('library/book/<ID>', views.book, name='book'),

]