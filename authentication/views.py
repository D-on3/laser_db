from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .utils import generate_api_token
from django.shortcuts import render, redirect




@login_required
def profile(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if created or not profile.api_token:
        profile.api_token = generate_api_token()
        profile.save()

    context = {'profile': profile}
    return render(request, 'authentication/profile.html', context)


from django.shortcuts import render, redirect
from .forms import UserProfileCreationForm, UserProfileLoginForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserProfileCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pages:home')  # Replace 'home' with your desired redirect URL
    else:
        form = UserProfileCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserProfileLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('pages:home')  # Replace 'home' with your desired redirect URL
    else:
        form = UserProfileLoginForm()
    return render(request, 'authentication/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('authentication:login')
