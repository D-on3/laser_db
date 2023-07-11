from django.contrib.auth.forms import AuthenticationForm
from django import forms
from accounts.models import CustomUser as User

class UserSignUpForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','password','email','first_name','last_name',)
		help_texts = {
			'username': None,
		}
		widgets = {
			'password':forms.PasswordInput(),
		}
		def clean(self):
			cleaned_data = super(TimesheetEntryForm, self).clean()
			print("hello")
			print("cleaned data")
			if cleaned_data.get('start_time') >= cleaned_data.get('end_time'):
				raise ValidationError("blah blah")

class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Username", max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
	password = forms.CharField(label="Password", max_length=30,widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
