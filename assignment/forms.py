from django import forms
from .models import Assignment, StudentAssignment, TeacherReview

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['course', 'title', 'description', 'file']

class StudentAssignmentForm(forms.ModelForm):
    class Meta:
        model = StudentAssignment
        fields = ['file']

class TeacherReviewForm(forms.ModelForm):
    class Meta:
        model = TeacherReview
        fields = ['grade', 'comments']
