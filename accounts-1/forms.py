from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import CustomUser

class LoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=100, label='Username or Email')
    password = forms.CharField(widget=forms.PasswordInput)

class LoginEmailForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

class LoginEmailOrUsernameForm(forms.Form):
    username_or_email = forms.CharField(max_length=100, label='Username or Email')
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'confirm_password', 'first_name', 'last_name')

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return confirm_password

class ResetPasswordEmailForm(forms.Form):
    email = forms.EmailField(label='Email')

class ResendActivationForm(forms.Form):
    email = forms.EmailField(label='Email')

class ChangePasswordForm(PasswordChangeForm):
    pass

class ChangeEmailForm(forms.Form):
    new_email = forms.EmailField(label='New Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

class ChangeProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')