from django import forms
from .models import Course, CourseVideos


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields=['course_name', 'description','field', 'image']


# class AddAssignment(forms.ModelForm):
#     class Meta:
#         model = AssignmentTeacher
#         fields = ['teacher','title', 'course', 'question']

#     labels = {
#         'teacher': 'Teacher',
#         'title': 'Assignment Title',
#         'course':'Assignment for course',
#         'question': 'Assignment',
#     }

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'field', 'description' ,'image']



class UploadForm(forms.ModelForm):
    class Meta:
        model = CourseVideos
        fields = ['title', 'video' ]