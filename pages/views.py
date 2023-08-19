from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import LaserMarkingParametersForm  # Import your form
from .models import LaserMarkingParameters, LaserSource


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def services(request):
    return render(request, 'pages/services.html')



@login_required
def search_laser_sources(request):
    if request.method == "GET":
        color_red = request.GET.get("color_red")
        color_green = request.GET.get("color_green")
        color_blue = request.GET.get("color_blue")

        if color_red is not None and color_green is not None and color_blue is not None:
            # Filter LaserMarkingParameters based on color channels
            laser_marking_params = LaserMarkingParameters.objects.filter(
                color_red=color_red,
                color_green=color_green,
                color_blue=color_blue
            )

            # Get unique LaserSource IDs from the filtered marking parameters
            laser_source_ids = laser_marking_params.values_list(
                "laser_source", flat=True).distinct()

            # Retrieve LaserSource objects based on the filtered IDs
            laser_sources = LaserSource.objects.filter(
                id__in=laser_source_ids)

            return render(request, "pages/laser_source_list.html",
                          {"laser_sources": laser_sources})

    # If no search was performed or no matching results found, display all LaserSource objects
    laser_sources = LaserSource.objects.all()
    return render(request, "pages/laser_source_list.html",
                  {"laser_sources": laser_sources})

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

@login_required
def laser_source_list(request):
    laser_sources = LaserSource.objects.all()
    return render(request, "pages/laser_source_list.html",
                  {"laser_sources": laser_sources})

@login_required
def laser_source_detail(request, pk):
    laser_source = get_object_or_404(LaserSource, pk=pk)
    return render(request, "pages/laser_source_detail.html",
                  {"laser_source": laser_source})
