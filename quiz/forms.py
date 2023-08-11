from django import forms
from .models import Quiz, Question, Option

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['course', 'quiz_name']

    labels = {
        "course":"course"
    }
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [ 'quiz' ,'content']

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['question','content', 'is_correct']
