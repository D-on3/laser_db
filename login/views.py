from django.shortcuts import render
from .models import Material, ColorOutcome, LaserParameter

def index(request):
    # Logic to retrieve and display laser parameters
    laser_parameters = LaserParameter.objects.all()
    context = {'laser_parameters': laser_parameters}
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