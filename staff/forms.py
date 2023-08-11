from django import forms
from django.contrib.auth.forms import AuthenticationForm


class ContactUsForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class TeacherSalaryForm(forms.Form):
    salary=forms.IntegerField()

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50)
    password = forms.PasswordInput()