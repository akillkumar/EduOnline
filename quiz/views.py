from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Quiz, Question, Option, UserResponse
from django.contrib.auth.decorators import login_required
from accounts.views import is_student, is_teacher
from .forms import QuizForm, QuestionForm, OptionForm
from accounts.models import Profile

def available_quizzes(request):
    quizzes = Quiz.objects.all()

    context = {
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        'quizzes': quizzes
        }
    return render(request, 'quiz/quizzes.html', context)



@login_required(login_url='login')
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz)

    context = {
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        'quiz': quiz,
        'questions': questions,
    }
    return render(request, 'quiz/quiz_detail.html', context)

@login_required(login_url='login')
def calculate_score(request, quiz_id):
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        questions = Question.objects.filter(quiz=quiz)
        total_questions = questions.count()
        score = 0

        for question in questions:
            selected_option_id = request.POST.get(f'question_{question.id}')
            if selected_option_id:
                selected_option = Option.objects.get(pk=selected_option_id)
                if selected_option.is_correct:
                    score += 1
                UserResponse.objects.create(user=request.user, question=question, selected_option=selected_option)

        messages.success(request, f'Your degrees is: {score} of {total_questions}')
        return redirect('quiz_detail', quiz_id=quiz_id)

    return redirect('quiz_detail', quiz_id=quiz_id)



def add_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('available_quizzes')  
    else:
        form = QuizForm()
    context =  {
        'form': form,
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),

        }
    return render(request, 'quiz/add_quiz.html',context)


def add_questions(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'added successfully...') 
            
    else:
        form = QuestionForm()

    context = {
        'form':form,
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),

    }
    return render(request, 'quiz/add_questions.html', context)

def add_options(request):
    if request.method == 'POST':
        form = OptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'added successfully...') 
    else:
        form = OptionForm()    
    context = {
        'form':form,
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),

    }
    return render(request, 'quiz/add_options.html', context)




def remove_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == 'POST':
        quiz.delete()
        return redirect('available_quizzes')  # Redirect to the list of quizzes
    context = {
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        'quiz': quiz,
        }
    return render(request, 'quiz/remove_quiz.html', context)


def edit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == 'POST':
        form = QuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            return redirect('available_quizzes')
    else:
        form = QuizForm(instance=quiz)
    context ={
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
        'form': form, 
        'quiz': quiz,
            }
    return render(request, 'quiz/edit_quiz.html', context)



@login_required(login_url='login')
def results_page(request):
    students = User.objects.all()
    context = {
        'students':students,
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
    }
    return render(request, 'quiz/results_page.html', context)


def result(request, student):
    try:
        user = User.objects.get(username=student)
        results = UserResponse.objects.filter(user=user)

    except:
        return redirect('results_page')
    context = {
        'results':results,
        'student':is_student(request.user),
        'teacher':is_teacher(request.user),
    }
    return render(request, 'quiz/result.html', context)
