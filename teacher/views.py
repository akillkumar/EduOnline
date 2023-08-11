from django.shortcuts import render, redirect
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta

from quiz.models import *
from student.models import Student
from course.forms import CourseForm
from course.models import Course


def teacher_signup(request):
    userForm=forms.TeacherUserForm()
    teacherForm=forms.TeacherForm()
    context = {'userForm':userForm,'teacherForm':teacherForm}
    if request.method=='POST':
        userForm=forms.TeacherUserForm(request.POST)
        teacherForm=forms.TeacherForm(request.POST,request.FILES)
        if userForm.is_valid() and teacherForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            teacher=teacherForm.save(commit=False)
            teacher.user=user
            teacher.save()
            my_teacher_group = Group.objects.get_or_create(name='TEACHER')
            my_teacher_group[0].user_set.add(user)
        return HttpResponseRedirect('login')
    return render(request,'teacher/teachersignup.html',context=context)



def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()


@login_required(login_url='login')
@user_passes_test(is_teacher)
def teacher_dashboard(request):
    teacher = is_teacher(request.user)
    context={
    'teacher':teacher,
    'total_course': Course.objects.all().count(),
    'total_student':Student.objects.all().count()
    }
    return render(request,'teacher/teacher_dashboard.html', context)

@login_required(login_url='login')
@user_passes_test(is_teacher)
def teacher_exam(request):
    return render(request,'teacher/teacher_exam.html')


@login_required(login_url='login')
@user_passes_test(is_teacher)
def teacher_add_exam(request):
    courseForm= CourseForm()
    if request.method=='POST':
        courseForm= CourseForm(request.POST)
        if courseForm.is_valid():        
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher/teacher-view-exam')
    return render(request,'teacher/teacher_add_exam.html',{'courseForm':courseForm})

@login_required(login_url='login')
@user_passes_test(is_teacher)
def teacher_view_exam(request):
    courses = Course.objects.all()
    return render(request,'teacher/teacher_view_exam.html',{'courses':courses})

@login_required(login_url='login')
@user_passes_test(is_teacher)
def delete_exam(request,pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/teacher/teacher-view-exam')

@login_required(login_url='login')
@user_passes_test(is_teacher)
def teacher_view_question(request):
    courses= Course.objects.all()
    return render(request,'teacher/teacher_view_question.html',{'courses':courses})

