from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Author, Machine, Result
from .forms import AuthorForm, MachineForm, ResultForm


@login_required
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form})


@login_required
def author_update(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if author.user != request.user:
        return redirect('author_list')
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author_form.html', {'form': form})


@login_required
def machine_create(request):
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            machine = form.save(commit=False)
            machine.user = request.user
            machine.save()
            return redirect('machine_list')
    else:
        form = MachineForm()
    return render(request, 'machine_form.html', {'form': form})


@login_required
def machine_update(request, machine_id):
    machine = get_object_or_404(Machine, pk=machine_id)
    if machine.user != request.user:
        return redirect('machine_list')
    if request.method == 'POST':
        form = MachineForm(request.POST, instance=machine)
        if form.is_valid():
            form.save()
            return redirect('machine_list')
    else:
        form = MachineForm(instance=machine)
    return render(request, 'machine_form.html', {'form': form})


@login_required
def result_create(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.user = request.user
            result.save()
            return redirect('result_list')
    else:
        form = ResultForm()
    return render(request, 'result_form.html', {'form': form})


@login_required
def result_update(request, result_id):
    result = get_object_or_404(Result, pk=result_id)
    if result.user != request.user:
        return redirect('result_list')
    if request.method == 'POST':
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            return redirect('result_list')
    else:
        form = ResultForm(instance=result)
    return render(request, 'result_form.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


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
