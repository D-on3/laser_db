from django.shortcuts import render, redirect
from .models import Material, ColorOutcome, LaserParameter
from .forms import LaserParameterForm

def index(request):
    laser_parameters = LaserParameter.objects.all()
    context = {'laser_parameters': laser_parameters}
    return render(request, 'index.html', context)

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

def delete_laser_parameter(request, laser_parameter_id):
    laser_parameter = LaserParameter.objects.get(id=laser_parameter_id)
    if request.method == 'POST':
        laser_parameter.delete()
        return redirect('index')
    context = {'laser_parameter': laser_parameter}
    return render(request, 'delete_laser_parameter.html', context)

def registration(request):
    # Handle user registration logic here
    return render(request, 'registration.html')

def login_view(request):
    # Handle user login logic here
    return render(request, 'login.html')