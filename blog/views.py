from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Article, Book
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from accounts.models import Profile
from .forms import AddArticle, ContactUsForm
from accounts.models import FeedBack
from accounts.views import is_student, is_teacher



def home(request):
    #if request.user.is_authenticated:
        #return redirect('profile', request.user)
    profile = Profile.objects.all()
    feedbacks = FeedBack.objects.all()
    courses = Course.objects.filter(field='FRONT-END')
                
    context = {
        "profile":profile,
        "feedbacks":feedbacks,
        "courses":courses,
    }
    return render(request,'blog/index.html', context)


def aboutUs(request):
    courses = Course.objects.all().count()
    students = Student.objects.all().count()
    staff = Profile.objects.all()

    context = {
        "courses":courses,
        "students":students,
        "staff":staff,
        
        }
    return render(request,'blog/about-us.html', context)


def contactUs(request):
    message = ''
    if request.method == 'POST':
        contact = ContactUsForm(request.POST)
        if contact.is_valid():
            contact.save()
            message = 'Thanks to contact us we will contact you soon...'
    else:
        contact = ContactUsForm()
    context = {
        'form':contact,
        'message':message,
    }
    return render(request, 'blog/contact-us.html', context)


def library(request):
    books = Book.objects.all()
    
    #profile = Student.objects.get(User=request.user)
    
    context = {
    #   "profile":profile,
        'teacher':is_teacher(request.user),
        'student':is_student(request.user),
        'books':books
    }
    return render(request, 'blog/library.html', context)

@login_required(login_url='login')
def book(request, ID):
    book = Book.objects.get(id=ID)
    #profile = Profile.objects.get(username=request.user)
    
    context = {
    #   "profile":profile,
        'teacher':is_teacher(request.user),
        'student':is_student(request.user),
        'book':book,
    }
    return render(request, 'blog/bookDetails.html', context)


def blog(request):
    articles = Article.objects.all()
    #profile = Profile.objects.get(username=request.user)

    context = {
        #   "profile":profile,
        'teacher':is_teacher(request.user),
        'student':is_student(request.user),
        'articles':articles,
    }
    return render(request, 'blog/blog.html', context)

@login_required(login_url='login')
def article(request, ID):
    profile = Profile.objects.get(username=request.user)
    article_details = Article.objects.get(id=ID)
    context = {
        'teacher':is_teacher(request.user),
        'student':is_student(request.user),
        'article':article_details,
        "profile":profile,
    }
    return render(request, 'blog/article.html', context)

@login_required(login_url='login')
def addArticle(request):
    if request.method == 'POST':
        form = AddArticle(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('blog')
    else:
        form = AddArticle
    context = {
        'teacher':is_teacher(request.user),
        'student':is_student(request.user),
        'form':form,
        }
    return render(request, 'blog/add-article.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')