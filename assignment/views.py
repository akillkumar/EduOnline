from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Assignment, StudentAssignment, TeacherReview
from .forms import AssignmentForm, StudentAssignmentForm, TeacherReviewForm
from accounts.views import is_student, is_teacher

def assignment_list(request):
    assignments = Assignment.objects.all()
    context = {
        'assignments': assignments,
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
    }
    return render(request, 'assignment/assignment_list.html', context)


def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment') 
    else:
        form = AssignmentForm()
    
    context = {
        'form': form,
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        }
    return render(request, 'assignment/add_assignment.html', context)

def student_upload_assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    if request.method == 'POST':
        form = StudentAssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            student_assignment = form.save(commit=False)
            student_assignment.student = request.user
            student_assignment.assignment = assignment
            student_assignment.save()
            return redirect('assignment')  # Replace 'assignment_list' with the URL name for the assignment list view
    else:
        form = StudentAssignmentForm()
    context = {
        'assignment': assignment,
        'form': form,
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        }
    return render(request, 'assignment/student_upload_assignment.html', context)


def review_assignment(request):

    student_assign = StudentAssignment.objects.all()

    context ={

        'assignments':student_assign,
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),

    }
    return render(request, 'assignment/review_assignment.html', context)



def teacher_review_assignment(request, assignmentId):
    student_assignment = StudentAssignment.objects.get(id=assignmentId)
    if request.method == 'POST':
        form = TeacherReviewForm(request.POST)
        if form.is_valid():
            teacher_review = form.save(commit=False)
            teacher_review.student_assignment = student_assignment
            teacher_review.teacher = request.user
            teacher_review.save()
            return redirect('assignment')
    else:
        form = TeacherReviewForm()
    
    context = {
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        'form': form,
        'student_assignment': student_assignment,
        }

    return render(request, 'assignment/teacher_review_assignment.html', context)



def results(request, user):
    student = User.objects.get(username=user)
    try:
        assign = StudentAssignment.objects.get(student=student)
    except:
        assign = None
    result = TeacherReview.objects.filter(student_assignment=assign)
    context = {
        'result':result,
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        
    }
    return render(request, 'assignment/results.html', context)


def edit_assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignment')
    else:
        form = AssignmentForm(instance=assignment)
    
    context = {
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        'form': form,
        'assignment': assignment}
    return render(request, 'assignment/edit_assignment.html', context)

def delete_assignment(request, assignment_id):
    if request.method == 'POST':
        assignment = Assignment.objects.get(id=assignment_id)
        assignment.delete()
        assignment.save()
    return redirect('assignment')