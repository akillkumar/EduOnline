from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required, user_passes_test

from . import forms,models
from quiz.models import *
from course.models import Course
from student.models import Student
from accounts.views import is_student


def student_signup_view(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.StudentForm()
    context ={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST,request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    
    return render(request,'student/studentsignup.html',context)

@login_required(login_url='login')
@user_passes_test(is_student)
def dashboard(request):
    context={
    'student':is_student(request.user),
    'total_course':Course.objects.all().count(),
    }
    return render(request,'student/student_dashboard.html', context)

