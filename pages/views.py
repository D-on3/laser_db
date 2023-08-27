from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import LaserSource
from .forms import LaserSourceForm, LaserMarkingParametersForm
from django.shortcuts import render
from .models import LaserMarkingParameters

from django.shortcuts import render
from .models import LaserMarkingParameters

def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')





from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Material, LaserSource, LaserMarkingParameters

@login_required
def material_list(request):
    materials = Material.objects.all()
    context = {'materials': materials}
    return render(request, 'pages/material_list.html', context)

@login_required
def laser_source_list(request):
    laser_sources = LaserSource.objects.all()
    context = {'laser_sources': laser_sources}
    return render(request, 'pages/laser_source_list.html', context)

@login_required
def laser_marking_parameters_list(request):
    marking_parameters = LaserMarkingParameters.objects.all()
    context = {'laser_marking_parameters': marking_parameters}
    return render(request, 'pages/laser_marking_parameters_list.html', context)
