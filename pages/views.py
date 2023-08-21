from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import LaserMarkingParametersForm  # Import your form
from .models import LaserMarkingParameters, LaserSource
# machines/views.py
from django.shortcuts import render, redirect
from .forms import LaserSourceForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import LaserSource
from .forms import LaserSourceForm

def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


@login_required
def create_machine(request):
    if request.method == 'POST':
        form = LaserSourceForm(request.POST)
        if form.is_valid():
            machine = form.save()  # Save the form data to create a new machine
            return redirect(
                'machine_list')  # Redirect to a page that lists machines
    else:
        form = LaserSourceForm()

    context = {'form': form}
    return render(request, 'pages/create_machine.html', context)

@login_required
def create_laser_marking_parameters(request):
    if request.method == 'POST':
        form = LaserMarkingParametersForm(request.POST)
        if form.is_valid():
            parameters = form.save(commit=False)
            parameters.date_published = timezone.now()  # Set current date as date_published
            parameters.research_date = timezone.now()  # Set current date as research_date
            parameters.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = LaserMarkingParametersForm()

    context = {'form': form}
    return render(request, 'pages/create_parameters.html', context)




from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import LaserSource, LaserMarkingParameters
from .forms import LaserSourceForm

# Views for LaserSource model
@login_required
def laser_source_list(request):
    laser_sources = LaserSource.objects.all()
    return render(request, 'pages/laser_source_list.html', {'laser_sources': laser_sources})

@login_required
def laser_source_detail(request, pk):
    laser_source = get_object_or_404(LaserSource, pk=pk)
    return render(request, 'pages/laser_source_detail.html', {'laser_source': laser_source})

@login_required
def create_laser_source(request):
    if request.method == 'POST':
        form = LaserSourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laser_source_list')
    else:
        form = LaserSourceForm()
    return render(request, 'pages/create_laser_source.html', {'form': form})

@login_required
def update_laser_source(request, pk):
    laser_source = get_object_or_404(LaserSource, pk=pk)
    if request.method == 'POST':
        form = LaserSourceForm(request.POST, instance=laser_source)
        if form.is_valid():
            form.save()
            return redirect('laser_source_detail', pk=pk)
    else:
        form = LaserSourceForm(instance=laser_source)
    return render(request, 'pages/update_laser_source.html', {'form': form, 'laser_source': laser_source})

@login_required
def delete_laser_source(request, pk):
    laser_source = get_object_or_404(LaserSource, pk=pk)
    if request.method == 'POST':
        laser_source.delete()
        return redirect('laser_source_list')
    return render(request, 'pages/delete_laser_source.html', {'laser_source': laser_source})

# Views for LaserMarkingParameters model
@login_required
def laser_marking_parameters_list(request):
    marking_parameters = LaserMarkingParameters.objects.all()
    return render(request, 'pages/laser_marking_parameters_list.html', {'marking_parameters': marking_parameters})

@login_required
def laser_marking_parameters_detail(request, pk):
    marking_parameters = get_object_or_404(LaserMarkingParameters, pk=pk)
    return render(request, 'pages/laser_marking_parameters_detail.html', {'marking_parameters': marking_parameters})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import LaserSource, LaserMarkingParameters
from .forms import LaserSourceForm, LaserMarkingParametersForm

# ... (Previous views for LaserSource model)

# Views for LaserMarkingParameters model
@login_required
def laser_marking_parameters_list(request):
    marking_parameters = LaserMarkingParameters.objects.all()
    return render(request, 'pages/laser_marking_parameters_list.html', {'marking_parameters': marking_parameters})

@login_required
def laser_marking_parameters_detail(request, pk):
    marking_parameters = get_object_or_404(LaserMarkingParameters, pk=pk)
    return render(request, 'pages/laser_marking_parameters_detail.html', {'marking_parameters': marking_parameters})

@login_required
def create_laser_marking_parameters(request):
    if request.method == 'POST':
        form = LaserMarkingParametersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laser_marking_parameters_list')
    else:
        form = LaserMarkingParametersForm()
    return render(request, 'pages/create_laser_marking_parameters.html', {'form': form})

@login_required
def update_laser_marking_parameters(request, pk):
    marking_parameters = get_object_or_404(LaserMarkingParameters, pk=pk)
    if request.method == 'POST':
        form = LaserMarkingParametersForm(request.POST, instance=marking_parameters)
        if form.is_valid():
            form.save()
            return redirect('laser_marking_parameters_detail', pk=pk)
    else:
        form = LaserMarkingParametersForm(instance=marking_parameters)
    return render(request, 'pages/update_laser_marking_parameters.html', {'form': form, 'marking_parameters': marking_parameters})

@login_required
def delete_laser_marking_parameters(request, pk):
    marking_parameters = get_object_or_404(LaserMarkingParameters, pk=pk)
    if request.method == 'POST':
        marking_parameters.delete()
        return redirect('laser_marking_parameters_list')
    return render(request, 'pages/delete_laser_marking_parameters.html', {'marking_parameters': marking_parameters})
