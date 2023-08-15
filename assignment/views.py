from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
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




@login_required
def exam_list(request):
    exams = Exam.objects.all()
    context = {
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        'exams': exams,
    }
    return render(request, 'exam/exam_list.html', context)

@login_required
def exam_page(request, exam_id):
    try:
        exam = Exam.objects.get(pk=exam_id)
        questions = ExamQuestion.objects.filter(exam=exam)
    except Exam.DoesNotExist:
        return redirect('exam_list')
    
    context = {
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        'exam': exam, 'questions': questions,
    }
    return render(request, 'exam/exam_page.html', context)

@login_required
def student_results(request):
    user = request.user
    results = ExamResult.objects.all()
    context = {
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        'results': results
    }
    return render(request, 'exam/student_results.html', context)

@login_required
def calculate_results(request, exam_id):
    if request.method == 'POST':
        try:
            exam = Exam.objects.get(pk=exam_id)
            questions = ExamQuestion.objects.filter(exam=exam)
        except Exam.DoesNotExist:
            return redirect('exam_list')

        degrees = 0
        for question in questions:
                answers = QuestionAnswer.objects.filter(question=question)
                answer_id = request.POST.get(f'question_{question.id}')
                for answer in answers:
                    if (answer_id in answer.answer):
                        degrees += 1
        
        print(request.user, degrees)

        new_result = ExamResult.objects.create(student=request.user,exam=exam, degrees=degrees)
        new_result.save()
        return HttpResponseRedirect(reverse('student_results'))

    return HttpResponseRedirect(reverse('exam_list'))