from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import LaserSource
from .forms import LaserSourceForm, LaserMarkingParametersForm
from django.shortcuts import render
from .models import LaserMarkingParameters


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
                'pages:machine_list')  # Redirect to a page that lists machines
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
            return redirect('pages:success_page')  # Redirect to a success page
    else:
        form = LaserMarkingParametersForm()

    context = {'form': form}
    return render(request, 'pages/create_parameters.html', context)


# Views for LaserSource model
@login_required
def laser_source_list(request):
    laser_sources = LaserSource.objects.all()
    return render(request, 'pages/laser_source_list.html',
                  {'laser_sources': laser_sources})


@login_required
def laser_source_detail(request, pk):
    laser_source = get_object_or_404(LaserSource, pk=pk)
    return render(request, 'pages/laser_source_detail.html',
                  {'laser_source': laser_source})


@login_required
def create_laser_source(request):
    if request.method == 'POST':
        form = LaserSourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:laser_source_list')
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
            return redirect('pages:laser_source_detail', pk=pk)
    else:
        form = LaserSourceForm(instance=laser_source)
    return render(request, 'pages/update_laser_source.html',
                  {'form': form, 'laser_source': laser_source})


@login_required
def delete_laser_source(request, pk):
    laser_source = get_object_or_404(LaserSource, pk=pk)
    if request.method == 'POST':
        laser_source.delete()
        return redirect('pages:laser_source_list')
    return render(request, 'pages/delete_laser_source.html',
                  {'laser_source': laser_source})


# Views for LaserMarkingParameters model
@login_required
def laser_marking_parameters_list(request):
    marking_parameters = LaserMarkingParameters.objects.all()
    return render(request, 'pages/laser_marking_parameters_list.html',
                  {'marking_parameters': marking_parameters})


@login_required
def laser_marking_parameters_detail(request, pk):
    marking_parameters = get_object_or_404(LaserMarkingParameters, pk=pk)
    return render(request, 'pages/laser_marking_parameters_detail.html',
                  {'marking_parameters': marking_parameters})


# ... (Previous views for LaserSource model)

# Views for LaserMarkingParameters model
@login_required
def laser_marking_parameters_list(request):
    marking_parameters = LaserMarkingParameters.objects.all()
    return render(request, 'pages/laser_marking_parameters_list.html',
                  {'marking_parameters': marking_parameters})


@login_required
def laser_marking_parameters_detail(request, pk):
    marking_parameters = get_object_or_404(LaserMarkingParameters, pk=pk)
    return render(request, 'pages/laser_marking_parameters_detail.html',
                  {'marking_parameters': marking_parameters})


@login_required
def create_laser_marking_parameters(request):
    if request.method == 'POST':
        form = LaserMarkingParametersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:laser_marking_parameters_list')
    else:
        form = LaserMarkingParametersForm()
    return render(request, 'pages/create_laser_marking_parameters.html',
                  {'form': form})


@login_required
def update_laser_marking_parameters(request, pk):
    marking_parameters = get_object_or_404(LaserMarkingParameters, pk=pk)
    if request.method == 'POST':
        form = LaserMarkingParametersForm(request.POST,
                                          instance=marking_parameters)
        if form.is_valid():
            form.save()
            return redirect('pages:laser_marking_parameters_detail', pk=pk)
    else:
        form = LaserMarkingParametersForm(instance=marking_parameters)
    return render(request, 'pages/update_laser_marking_parameters.html',
                  {'form': form, 'marking_parameters': marking_parameters})


@login_required
def delete_laser_marking_parameters(request, pk):
    marking_parameters = get_object_or_404(LaserMarkingParameters, pk=pk)
    if request.method == 'POST':
        marking_parameters.delete()
        return redirect('pages:laser_marking_parameters_list')
    return render(request, 'pages/delete_laser_marking_parameters.html',
                  {'marking_parameters': marking_parameters})


def search_by_color(request):
    if request.method == 'POST':
        # Assuming you have a form with 'color' field
        color = request.POST.get('color')

        # Perform the color search logic here
        parameters_with_color = LaserMarkingParameters.objects.filter(
            color_red=color[0], color_green=color[1], color_blue=color[2]
        )

        context = {'parameters_with_color': parameters_with_color,
                   'color': color}
    else:
        context = {}

    return render(request, 'pages/search_by_color.html', context)
