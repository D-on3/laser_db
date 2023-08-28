
from django.shortcuts import  get_object_or_404
from pages.models import Material, LaserSource

from django.urls import reverse_lazy
from django.views.generic import  UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from .forms import GaeParamsForm
from .models import LaserMarkingParameters  # Import your model
from .utils import ColorSpectrum  # Import your ColorSpectrum class


@method_decorator(login_required, name='dispatch')
class UpdateView(UpdateView):
    model = LaserMarkingParameters
    template_name = 'laser_parameters_update.html'  # Create a template for update view
    fields = '__all__'  # You can customize which fields to display and update


@method_decorator(login_required, name='dispatch')
class DeleteView(DeleteView):
    model = LaserMarkingParameters
    template_name = 'delete.html'  # Create a template for delete confirmation
    success_url = reverse_lazy(
        'pages:list_view')  # Redirect after successful deletion


import colorsys
from .forms import GaeParamsForm
from .models import LaserMarkingParameters, Material, LaserSource
from django.shortcuts import render
from .utils import ColorSpectrum,hex_to_rgb

# Define the rgb_values for your samples
rgb_values = [
    (255, 0, 0),     # red
    (255, 165, 0),   # orange
    (255, 255, 0),   # yellow
    (0, 128, 0),     # green
    (0, 0, 255),     # blue
    (75, 0, 130),    # indigo
    (238, 130, 238), # violet
]

from .forms import GaeParamsForm
from .utils import ColorSpectrum
from django.shortcuts import render
from django.db.models import Q
from collections import Counter

def search_results(request):
    form = GaeParamsForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            hex_color = form.cleaned_data['hex_color']
            hex_color = hex_color.lstrip('#')
            rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

            if len(rgb_color) != 3:
                return render(request, 'pages/search_color.html', {'form': form, 'error_message': 'Invalid RGB color'})

            form_color = ColorSpectrum([rgb_color]).classify_colors_by_spectrum()
            filtered_dict = {key: value for key, value in form_color.items() if value}
            print(filtered_dict)

            all_colors_in_db = LaserMarkingParameters.objects.all()

            matching_colors = []
            for current_color in all_colors_in_db:
                current_color_classifier = ColorSpectrum([
                    (current_color.color_red, current_color.color_green, current_color.color_blue)
                ]).classify_colors_by_spectrum()
                current_color_classifier = {key: value for key, value in current_color_classifier.items() if value}

                if current_color_classifier.keys() == filtered_dict.keys():
                    matching_colors.append(current_color)

            return render(request, 'pages/matching_colors.html', {'form': form, 'matching_colors': matching_colors})

    return render(request, 'pages/search_color.html', {'form': form})
def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


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
    print(context)
    return render(request, 'pages/laser_marking_parameters_list.html',
                  context)


@login_required
def laser_marking_parameters_detail(request, pk):
    marking_parameters = get_object_or_404(LaserMarkingParameters, pk=pk)
    context = {'marking_parameters': marking_parameters}
    return render(request, 'pages/laser_marking_parameters_detail.html',
                  context)
