from django.shortcuts import render
from django.shortcuts import render
from .forms import LaserMarkingForm
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def services(request):
    return render(request, 'pages/services.html')


def add_laser_marking(request):
    if request.method == 'POST':
        form = LaserMarkingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LaserMarkingForm()
    return render(request, 'pages/add_result.html', {'form': form})