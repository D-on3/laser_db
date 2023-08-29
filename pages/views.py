from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView


from .forms import (
    GaeParamsForm,

    LaserSourceForm,
    MaterialForm,
    AddSampleForm
)

from .models import (
    LaserMarkingParameters,
    Material,
    LaserSource
)

from .utils import (
    ColorSpectrum,

)

# Define the rgb_values for your samples
rgb_values = [
    (255, 0, 0),  # red
    (255, 165, 0),  # orange
    (255, 255, 0),  # yellow
    (0, 128, 0),  # green
    (0, 0, 255),  # blue
    (75, 0, 130),  # indigo
    (238, 130, 238),  # violet
]


def add_sample(request):
    if request.method == 'POST':
        form = AddSampleForm(request.POST)
        if form.is_valid():
            # Create a new instance of LaserMarkingParameters using the form data
            laser_marking_parameters = LaserMarkingParameters(
                laser_source=form.cleaned_data['laser_source'],
                material=form.cleaned_data['material'],
                scanning_speed=form.cleaned_data['scanning_speed'],
                average_power=form.cleaned_data['average_power'],
                scan_step=form.cleaned_data['scan_step'],
                pulse_duration=form.cleaned_data['pulse_duration'],
                pulse_repetition_rate=form.cleaned_data[
                    'pulse_repetition_rate'],
                focus=form.cleaned_data['focus'],
                color_red=form.cleaned_data['color_red'],
                color_green=form.cleaned_data['color_green'],
                color_blue=form.cleaned_data['color_blue'],
                authors=form.cleaned_data['authors'],
                research_date=form.cleaned_data['research_date']
            )
            laser_marking_parameters.save()
            return redirect(
                'pages:matching_colors')  # Replace with your URL name
    else:
        form = AddSampleForm()

    return render(request, 'pages/laser_markin_parameters/add_sample.html', {'form': form})


def update_material(request, pk):
    material = get_object_or_404(Material, pk=pk)

    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('pages:laser_marking_parameters_list')
    else:
        form = MaterialForm(instance=material)

    return render(request, 'pages/materials/update_material.html', {'form': form})


def delete_material(request, pk):
    material = get_object_or_404(Material, pk=pk)

    if request.method == 'POST':
        material.delete()
        return redirect('pages:laser_marking_parameters_list')

    return render(request, 'pages/materials/delete_material.html',
                  {'material': material})


def add_laser_source(request):
    if request.method == 'POST':
        form = LaserSourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                'pages:add_sample')  # Redirect to the main add sample page
    else:
        form = LaserSourceForm()
    return render(request, 'pages/laser_sources/add_laser_source.html', {'form': form})

from django.shortcuts import render
from .utils import run_utils

def run_util_code_view(request):
    run_utils()  # Call the function from utils.py
    return render(request, 'pages/run_util_code.html')

def add_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                'pages:add_sample')  # Redirect to the main add sample page
    else:
        form = MaterialForm()
    return render(request, 'pages/materials/add_material.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class UpdateView(UpdateView):
    model = LaserMarkingParameters
    template_name = 'pages/laser_markin_parameters/laser_parameters_update.html'  # Create a template for update view
    success_url = reverse_lazy(
        'pages:laser_marking_parameters_list')  # Redirect after successful deletion
    fields = '__all__'  # You can customize which fields to display and update



# List view
def laser_source_list(request):
    laser_sources = LaserSource.objects.all()
    return render(request, 'pages/laser_sources/laser_source_list.html', {'laser_sources': laser_sources})

# Update view
class LaserSourceUpdateView(UpdateView):
    model = LaserSource
    form_class = LaserSourceForm
    template_name = 'pages/laser_sources/laser_source_form.html'  # Update with your template path
    success_url = reverse_lazy('pages:laser_source_list')  # Update with your URL name

# Delete view
class LaserSourceDeleteView(DeleteView):
    model = LaserSource
    success_url = reverse_lazy('pages:laser_source_list')  # Update with your URL name

@method_decorator(login_required, name='dispatch')
class DeleteView(DeleteView):
    model = LaserMarkingParameters
    template_name = 'pages/laser_markin_parameters/laser_parameters_delete.html'  # Create a template for delete confirmation
    success_url = reverse_lazy(
        'pages:laser_marking_parameters_list')  # Redirect after successful deletion


def search_results(request):
    form = GaeParamsForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            hex_color = form.cleaned_data['hex_color']
            hex_color = hex_color.lstrip('#')
            rgb_color = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

            if len(rgb_color) != 3:
                return render(request, 'pages/search_logic/search_color.html',
                              {'form': form,
                               'error_message': 'Invalid RGB color'})

            form_color = ColorSpectrum(
                [rgb_color]).classify_colors_by_spectrum()
            filtered_dict = {key: value for key, value in form_color.items()
                             if value}
            print(filtered_dict)

            all_colors_in_db = LaserMarkingParameters.objects.all()

            matching_colors = []
            for current_color in all_colors_in_db:
                current_color_classifier = ColorSpectrum([
                    (current_color.color_red, current_color.color_green,
                     current_color.color_blue)
                ]).classify_colors_by_spectrum()
                current_color_classifier = {key: value for key, value in
                                            current_color_classifier.items()
                                            if value}

                if current_color_classifier.keys() == filtered_dict.keys():
                    matching_colors.append(current_color)

            return render(request, 'pages/search_logic/matching_colors.html',
                          {'form': form, 'matching_colors': matching_colors})

    return render(request, 'pages/search_logic/search_color.html', {'form': form})


def home(request):
    return render(request, 'pages/views/home.html')


def about(request):
    return render(request, 'pages/views/about.html')


def contact(request):
    return render(request, 'pages/views/contact.html')


@login_required
def material_list(request):
    materials = Material.objects.all()
    context = {'materials': materials}
    return render(request, 'pages/materials/material_list.html', context)


@login_required
def laser_source_list(request):
    laser_sources = LaserSource.objects.all()
    context = {'laser_sources': laser_sources}
    return render(request, 'pages/laser_sources/laser_source_list.html', context)


@login_required
def laser_marking_parameters_list(request):
    marking_parameters = LaserMarkingParameters.objects.all()

    context = {'laser_marking_parameters': marking_parameters}
    print(context)
    return render(request,
                  'pages/laser_markin_parameters/laser_marking_parameters_list.html',
                  context)


@login_required
def laser_marking_parameters_detail(request, pk):
    marking_parameters = get_object_or_404(LaserMarkingParameters, pk=pk)
    context = {'marking_parameters': marking_parameters}
    return render(request,
                  'pages/laser_markin_parameters/laser_marking_parameters_detail.html',
                  context)
