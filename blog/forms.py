from django import forms
from .models import *

class AddArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        'image': forms.FileInput(attrs={'class': 'form-control-file'}),
    }

    labels = {
        'title': 'Article Title',
        'content': 'Article Content',
        'image': 'Article Image',
    }

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['firstName', 'lastName', 'email', 'message']

    # Specify the widget attributes
    widgets = {
        'firstName': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name',
            'required': True,
        }),
        'lastName': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name',
            'required': True,
        }),
        'email': forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@gmail.com',
            'required': True,
        }),
        'message': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Write your message here...',
            'rows': 4,
            'required': True,
        }),
    }


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']