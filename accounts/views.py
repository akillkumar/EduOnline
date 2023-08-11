from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from teacher.models import Teacher
from .forms import *
from django.contrib.auth.models import User, Group
from .models import Profile

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')[0]
            user.groups.add(my_student_group)

            # Redirect to login page after successful registration
            return redirect('login')  
    else:
        form = RegistrationForm()

    return render(request, 'account/registration.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile', request.user)
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'account/login.html', context)


def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

def is_superuser(user):
    return user.groups.filter(name='STUDENT').exists()


def afterLogin(request):
    if is_student(request.user):      
        return redirect('student')

    elif is_teacher(request.user):
        accountApproval= Teacher.objects.all().filter(user_id=request.user.id,status=True)
        if accountApproval:
            return redirect('teacher')
        else:
            return render(request,'teacher/teacher_wait_for_approval.html')
    else:
        return redirect('/staff/')
    
@login_required(login_url='login')
def edit_profile(request, user):
    profile = Profile.objects.get(username=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', request.user)  
    else:
        form = ProfileForm(instance=profile)
    
    context = {
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        'form': form
    }
    return render(request, 'account/edit_profile.html',context)


@login_required(login_url='login')
def edit_user_data(request, user):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile', user)
        else:
            messages.error(request,'Enter valid data')
    else:
        user_form = EditUserForm(instance=request.user)

    context = {
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        'form':user_form,
        user:request.user
    }
    return render(request, 'account/edit_user_data.html', context)

@login_required(login_url='login')
def profile(request, user):
    user = User.objects.get(username=user)
    user_profile = Profile.objects.get(username=user)
    context = {
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        'user':user, 
        'profile':user_profile,
    }
    return render(request, 'account/profile.html', context)




def signup(request):
    return render(request, 'account/signup.html')



@login_required(login_url='login')
def feedback(request, user):
    user_profile = Profile.objects.get(username=request.user.id)
    if request.method == 'POST':
        feedback_form = FeedBackForm(request.POST)
        rate = request.POST['course_rate']
        if feedback_form.is_valid():
            feedback_content = feedback_form.save(commit=False)
            feedback_content.user = user_profile
            feedback_content.course_rate = rate
            feedback_content.save()
            messages.success(request, 'Thanks to give us your feedback, best wishes')
        else:
            messages.success(request, 'Enter a valid data')

    else:
        feedback_form = FeedBackForm()
    context = {
        'profile':user_profile,
        'feedback':feedback_form,
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
    }
    return render(request, 'account/feedback.html', context)




@login_required(login_url='login')
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')