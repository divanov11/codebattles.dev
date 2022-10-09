from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Submission, User
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'name', 'email', 'avatar' ,'bio', 'twitter', 'linkedin', 'facebook', 'github', 'website']    
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-field--input'}),
            'name':forms.TextInput(attrs={'class':'form-field--input'}),
            'email':forms.EmailInput(attrs={'class':'form-field--input'}),
            'bio':forms.Textarea(attrs={'class':'form-field--input-txarea'}),
            'twitter': forms.TextInput(attrs={'class':'form-field--input'}),
            'linkedin':forms.TextInput(attrs={'class':'form-field--input'}),
            'facebook':forms.TextInput(attrs={'class':'form-field--input'}),
            'github':forms.TextInput(attrs={'class':'form-field--input'}),
            'website':forms.TextInput(attrs={'class':'form-field--input'})
        }
class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['details']
# 
class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password1', 'password2', 'avatar']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-field--input'}),
            'name':forms.TextInput(attrs={'class':'form-field--input'}),
            'email':forms.EmailInput(attrs={'class':'form-field--input'})
        }