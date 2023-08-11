from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from teacher.views import is_teacher
from django.db.models import Sum
from teacher.models import Teacher
from teacher.forms import TeacherForm, TeacherUserForm 
from student.models import Student
from course.models import Course

from .forms import ContactUsForm, TeacherSalaryForm
from student.forms import StudentForm, StudentUserForm
# from teacher.forms import TeacherForm, TeacherUserForm
from course.forms import CourseForm




def staffClick(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('after-login')
    return HttpResponseRedirect('login')



@login_required(login_url='login')
def dashboard(request):
    context = {
    'total_student':Student.objects.all().count(),
    'total_teacher':Teacher.objects.all().filter(status=True).count(),
    'total_course':Course.objects.all().count(),
    }
    return render(request,'staff/dashboard.html',context)


@login_required(login_url='login')
def staff_teacher(request):
    context={
    'total_teacher':Teacher.objects.all().filter(status=True).count(),
    'pending_teacher':Teacher.objects.all().filter(status=False).count(),
    'salary':Teacher.objects.all().filter(status=True).aggregate(Sum('salary'))['salary__sum'],
    }
    return render(request,'staff/teacher.html', context)



@login_required(login_url='login')
def staff_teacher(request):
    teachers= Teacher.objects.all().filter(status=True)
    return render(request,'staff/teacher.html',{'teachers':teachers})


@login_required(login_url='login')
def update_teacher(request,pk):
    teacher=Teacher.objects.get(id=pk)
    user=User.objects.get(id=teacher.user_id)
    userForm= TeacherUserForm(instance=user)
    teacherForm= TeacherForm(request.FILES,instance=teacher)
    context={'userForm':userForm,'teacherForm':teacherForm}
    
    if request.method=='POST':
        userForm= TeacherUserForm(request.POST,instance=user)
        teacherForm= TeacherForm(request.POST,request.FILES,instance=teacher)
        if userForm.is_valid() and teacherForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            teacherForm.save()
            return redirect('staff-view-teacher')
    return render(request,'quiz/update_teacher.html',context=context)




@login_required(login_url='login')
def delete_teacher(request,pk):
    teacher=Teacher.objects.get(id=pk)
    user=User.objects.get(id=teacher.user_id)
    user.delete()
    teacher.delete()
    return HttpResponseRedirect('/staff-view-teacher')





@login_required(login_url='login')
def staff_pending_teacher(request):
    teachers= Teacher.objects.all().filter(status=False)
    return render(request,'staff/pending_teacher.html',{'teachers':teachers})



@login_required(login_url='login')
def approve_teacher(request,pk):
    teacherSalary=TeacherSalaryForm()
    if request.method=='POST':
        teacherSalary=TeacherSalaryForm(request.POST)
        if teacherSalary.is_valid():
            teacher=Teacher.objects.get(id=pk)
            teacher.salary=teacherSalary.cleaned_data['salary']
            teacher.status=True
            teacher.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/staff-view-pending-teacher')
    return render(request,'quiz/salary_form.html',{'teacherSalary':teacherSalary})

@login_required(login_url='login')
def reject_teacher(request,pk):
    teacher=Teacher.objects.get(id=pk)
    user=User.objects.get(id=teacher.user_id)
    user.delete()
    teacher.delete()
    return HttpResponseRedirect('/staff-view-pending-teacher')

@login_required(login_url='login')
def staff_teacher_salary(request):
    teachers= Teacher.objects.all().filter(status=True)
    return render(request,'staff/teacher_salary.html',{'teachers':teachers})




@login_required(login_url='login')
def staff_student(request):
    context={
    'total_student':Student.objects.all().count(),
    }
    return render(request,'staff/staff_view_student.html',context=context)


@login_required(login_url='login')
def staff_student(request):
    students= Student.objects.all()
    return render(request,'staff/admin_view_student.html',{'students':students})



@login_required(login_url='login')
def update_student(request,pk):
    student=Student.objects.get(id=pk)
    user=User.objects.get(id=student.user_id)
    userForm= StudentUserForm(instance=user)
    studentForm= StudentForm(request.FILES,instance=student)
    context ={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm= StudentUserForm(request.POST,instance=user)
        studentForm= StudentForm(request.POST,request.FILES,instance=student)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            studentForm.save()
            return redirect('staff-view-student')
    return render(request,'quiz/update_student.html',context=context)



@login_required(login_url='login')
def delete_student(request,pk):
    student=Student.objects.get(id=pk)
    user=User.objects.get(id=student.user_id)
    user.delete()
    student.delete()
    return HttpResponseRedirect('/staff-view-student')


@login_required(login_url='login')
def staff_course(request):
    courses = Course.objects.all()
    return render(request,'staff/course.html', {'courses':courses})


@login_required(login_url='login')
def addCourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm()
    
    context = {
        'form': form,
        'teacher': is_teacher(request.user)
                }
    return render(request,'courses/add_course.html', context)


@login_required(login_url='login')
def staff_course(request):
    courses = Course.objects.all()
    return render(request,'staff/course.html',{'courses':courses})

@login_required(login_url='login')
def delete_course(request,pk):
    course=Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/staff-view-course')


