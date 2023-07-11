from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login
from django.contrib.auth.forms import PasswordChangeForm
from accounts import forms
from django.urls import reverse

def register(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			form = forms.UserSignUpForm(request.POST)
			if form.is_valid():
				user = form.save(commit=False)
				user.password = make_password(form.cleaned_data['password'])
				user.email = form.cleaned_data['email']
				user.save()
				login(request, user)
				return render(request,"register_succesful.html")
		else:
			form = forms.UserSignUpForm()
		return render(request,'accounts/register.html',context={
			'form':form
		})
	else:
		return redirect('/')

def change_password(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = PasswordChangeForm(request.user, request.POST)
			print(request.POST)
			if form.is_valid():
				user = form.save()
				update_session_auth_hash(request, user)
				return render(request,"password_change_succesful.html")
		else:
			form = PasswordChangeForm(request.user)
		return render(request, 'accounts/change_password.html', {
			'form': form
		})
	else:
		return redirect('/')
