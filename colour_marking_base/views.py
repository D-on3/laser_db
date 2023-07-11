from django.shortcuts import render
from .models import Material, ColorOutcome, LaserParameter

from django.core.paginator import Paginator


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid username or password'
            context = {'error_message': error_message}
            return render(request, 'login.html', context)
    return render(request, 'login.html')

def index(request):
    laser_parameters = LaserParameter.objects.all()
    paginator = Paginator(laser_parameters, 10)  # Display 10 laser parameters per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'index.html', context)


from django.shortcuts import render, redirect
from .models import Material, ColorOutcome, LaserParameter
from .forms import LaserParameterForm

def create_laser_parameter(request):
    if request.method == 'POST':
        form = LaserParameterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LaserParameterForm()
    context = {'form': form}
    return render(request, 'create_laser_parameter.html', context)


def edit_laser_parameter(request, laser_parameter_id):
    laser_parameter = LaserParameter.objects.get(id=laser_parameter_id)
    if request.method == 'POST':
        form = LaserParameterForm(request.POST, instance=laser_parameter)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LaserParameterForm(instance=laser_parameter)
    context = {'form': form}
    return render(request, 'edit_laser_parameter.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from .models import LaserParameter

def delete_laser_parameter(request, laser_parameter_id):
    laser_parameter = get_object_or_404(LaserParameter, id=laser_parameter_id)
    if request.method == 'POST':
        laser_parameter.delete()
        return redirect('index')
    context = {'laser_parameter': laser_parameter}
    return render(request, 'delete_laser_parameter.html', context)

from django.db.models import Q

def search(request):
    query = request.GET.get('q')
    laser_parameters = LaserParameter.objects.filter(
        Q(material__icontains=query) |
        Q(color_outcome__icontains=query)
    )
    context = {'laser_parameters': laser_parameters, 'query': query}
    return render(request, 'search.html', context)


import matplotlib.pyplot as plt

def visualization(request):
    color_outcomes = ColorOutcome.objects.all()
    outcomes = [outcome.name for outcome in color_outcomes]
    parameter_counts = LaserParameter.objects.values('color_outcome').annotate(count=models.Count('color_outcome'))
    counts = [count['count'] for count in parameter_counts]

    plt.bar(outcomes, counts)
    plt.xlabel('Color Outcome')
    plt.ylabel('Parameter Count')
    plt.title('Distribution of Laser Parameters by Color Outcome')
    plt.xticks(rotation=45)

    # Save the plot to a file or render it directly in the template

    # Example: save the plot to a file
    plt.savefig('path/to/visualization.png')

    return render(request, 'visualization.html')