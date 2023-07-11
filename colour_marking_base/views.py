from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import ColorOutcome, LaserParameter
from .forms import LaserParameterForm

@login_required(login_url='login')
def index(request):
    laser_parameters = LaserParameter.objects.filter(user=request.user)
    context = {'laser_parameters': laser_parameters}
    return render(request, 'index.html', context)


@login_required(login_url='login')
def create_laser_parameter(request):
    if request.method == 'POST':
        form = LaserParameterForm(request.POST)
        if form.is_valid():
            laser_parameter = form.save(commit=False)
            laser_parameter.user = request.user
            laser_parameter.save()
            return redirect('index')
    else:
        form = LaserParameterForm()
    context = {'form': form}
    return render(request, 'create_laser_parameter.html', context)


@login_required(login_url='login')
def edit_laser_parameter(request, laser_parameter_id):
    laser_parameter = LaserParameter.objects.get(id=laser_parameter_id)
    if laser_parameter.user == request.user:
        if request.method == 'POST':
            form = LaserParameterForm(request.POST, instance=laser_parameter)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = LaserParameterForm(instance=laser_parameter)
        context = {'form': form}
        return render(request, 'edit_laser_parameter.html', context)
    else:
        return redirect('index')


@login_required(login_url='login')
def delete_laser_parameter(request, laser_parameter_id):
    laser_parameter = LaserParameter.objects.get(id=laser_parameter_id)
    if laser_parameter.user == request.user:
        if request.method == 'POST':
            laser_parameter.delete()
            return redirect('index')
        context = {'laser_parameter': laser_parameter}
        return render(request, 'delete_laser_parameter.html', context)
    else:
        return redirect('index')


def search(request):
    query = request.GET.get('query')
    laser_parameters = LaserParameter.objects.filter(
        material__icontains=query)
    context = {'laser_parameters': laser_parameters, 'query': query}
    return render(request, 'search.html', context)


def visualization(request):
    color_outcomes = ColorOutcome.objects.all()
    outcomes = [outcome.name for outcome in color_outcomes]
    counts = [LaserParameter.objects.filter(color_outcome=outcome).count() for
              outcome in color_outcomes]
    context = {'outcomes': outcomes, 'counts': counts}
    return render(request, 'visualization.html', context)


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login


def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            # Check if the username is available
            if User.objects.filter(username=username).exists():
                error_message = 'Username is already taken. Please choose a different one.'
            else:
                try:
                    # Create a new user
                    user = User.objects.create_user(username=username,
                                                    password=password)
                    # Perform any additional user registration logic here
                    # For example, you might want to create a user profile or send a confirmation email

                    # Log in the newly registered user
                    login(request, user)

                    # Redirect the user to a success page or the desired destination
                    return redirect('index')
                except Exception as e:
                    error_message = 'An error occurred during registration. Please try again later.'
                    # You can log the error or handle it in any way you prefer
        else:
            error_message = 'Passwords do not match.'

        context = {'error_message': error_message}
        return render(request, 'registration.html', context)
    else:
        return render(request, 'registration.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User authentication successful
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid username or password.'

        context = {'error_message': error_message}
        return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')
