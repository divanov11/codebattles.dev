from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Submission, User

class UserForm(ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'name', 'email', 'avatar' ,'bio', 'twitter', 'linkedin', 'facebook', 'github', 'website']


class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['details']

class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password1', 'password2']