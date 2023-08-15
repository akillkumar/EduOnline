from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import *
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "first_name","last_name", "email", "password1", "password2"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'address', 'mobile']





class EditUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields =  ['username', 'first_name', 'last_name', 'email']



class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['content','course', 'course_rate']
