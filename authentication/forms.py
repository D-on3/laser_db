from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserProfileCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'username', 'password1', 'password2', 'profile_picture', 'bio']

class UserProfileLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
