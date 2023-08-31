from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import render
from .forms import RGBSearchForm
from .models import LaserMarkingParameters

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
    """
    The function `add_sample` is a view function that handles the submission of a
    form to add a new instance of `LaserMarkingParameters` to the database.

    :param request: The `request` parameter is an object that represents the HTTP
    request made by the client. It contains information such as the request method
    (GET, POST, etc.), headers, cookies, and the request body. In this code
    snippet, the `request` object is used to handle a form submission
    :return: a rendered HTML template with the form as context data.
    """
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
                'laser_color_marking_db:matching_colors')  # Replace with your URL name
    else:
        form = AddSampleForm()

    return render(request,
                  'laser_color_marking_db/laser_markin_parameters/add_sample.html',
                  {'form': form})


def update_material(request, pk):
    """
    The function updates a material object based on a POST request, or renders a
    form to update the material if the request method is not POST.

    :param request: The `request` parameter is an object that represents the HTTP
    request made by the client. It contains information such as the HTTP method
    used (e.g., GET, POST), the headers, the user making the request, and any data
    sent with the request
    :param pk: The "pk" parameter in the "update_material" function is the primary
    key of the Material object that needs to be updated. It is used to retrieve
    the specific Material object from the database using the "get_object_or_404"
    function
    :return: a rendered HTML template with the form as a context variable.
    """
    material = get_object_or_404(Material, pk=pk)

    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('pages:laser_marking_parameters_list')
    else:
        form = MaterialForm(instance=material)

    return render(request,
                  'laser_color_marking_db/materials/update_material.html',
                  {'form': form})


def delete_material(request, pk):
    material = get_object_or_404(Material, pk=pk)

    if request.method == 'POST':
        material.delete()
        return redirect('pages:laser_marking_parameters_list')

    return render(request,
                  'laser_color_marking_db/materials/delete_material.html',
                  {'material': material})


def add_laser_source(request):
    """
    The function `add_laser_source` is a view function that handles the creation
    of a new laser source object and redirects to the main add sample page if the
    form is valid.

    :param request: The request object represents the HTTP request made by the
    client. It contains information such as the HTTP method (GET, POST, etc.),
    headers, and data
    :return: a rendered HTML template with the form as context data.
    """
    if request.method == 'POST':
        form = LaserSourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                'pages:add_sample')  # Redirect to the main add sample page
    else:
        form = LaserSourceForm()
    return render(request,
                  'laser_color_marking_db/laser_sources/add_laser_source.html',
                  {'form': form})


from django.shortcuts import render
from .utils import run_utils


def run_util_code_view(request):
    """
    The function `run_util_code_view` calls a function from `utils.py` and renders
    a template called `run_util_code.html`.

    :param request: The request parameter is an object that represents the HTTP
    request made by the client. It contains information such as the HTTP method
    (GET, POST, etc.), headers, and any data sent with the request. It is
    typically passed to view functions in Django to handle the request and
    generate a response
    :return: a rendered HTML template called 'run_util_code.html'.
    """
    run_utils()  # Call the function from utils.py
    return render(request, 'laser_color_marking_db/run_util_code.html')


def add_material(request):
    """
    The function `add_material` is a view function in Django that handles the
    creation of a new material object and redirects to the main add sample page if
    the form is valid.

    :param request: The request object represents the HTTP request made by the
    client. It contains information such as the HTTP method (GET, POST, etc.),
    headers, and any data sent with the request
    :return: a rendered HTML template called 'add_material.html' with the form
    variable passed as context data.
    """
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            # Get material name from the form
            material_name = form.cleaned_data['name']

            # Try to get the material by name or create if it doesn't exist
            material, created = Material.objects.get_or_create(
                name=material_name)

            if created:
                return redirect(
                    'pages:add_sample')  # Redirect to the main add sample page
            else:
                # Material with the same name already exists
                form.add_error('name',
                               'Material with this name already exists.')
    else:
        form = MaterialForm()

    return render(request,
                  'laser_color_marking_db/materials/add_material.html',
                  {'form': form})


def search_by_rgb(request):
    form = RGBSearchForm(request.POST or None)
    results = None

    if form.is_valid():
        red = form.cleaned_data['red']
        green = form.cleaned_data['green']
        blue = form.cleaned_data['blue']

        results = LaserMarkingParameters.objects.filter(
            color_red=red, color_green=green, color_blue=blue
        )

    context = {'form': form, 'results': results}
    return render(request,
                  'laser_color_marking_db/search_logic/search_by_rgb.html', context)


@method_decorator(login_required, name='dispatch')
# The UpdateView class is used for updating an existing object in a Django
# application.
class UpdateView(UpdateView):
    model = LaserMarkingParameters
    template_name = 'laser_color_marking_db/laser_markin_parameters/laser_parameters_update.html'  # Create a template for update view
    success_url = reverse_lazy(
        'pages:laser_marking_parameters_list')  # Redirect after successful deletion
    fields = '__all__'  # You can customize which fields to display and update


# List view
def laser_source_list(request):
    """
    The function `laser_source_list` retrieves all laser sources from the database
    and renders them in a template called 'laser_source_list.html'.

    :param request: The request parameter is an object that represents the HTTP
    request made by the user. It contains information such as the user's browser,
    IP address, and any data sent with the request
    :return: a rendered HTML template called 'laser_source_list.html' with a
    context variable 'laser_sources' which contains all the LaserSource objects.
    """
    laser_sources = LaserSource.objects.all()
    return render(request,
                  'laser_color_marking_db/laser_sources/laser_source_list.html',
                  {'laser_sources': laser_sources})


# Update view
# The LaserSourceUpdateView class is a view used for updating laser source
# objects.
class LaserSourceUpdateView(UpdateView):
    model = LaserSource
    form_class = LaserSourceForm
    template_name = 'laser_color_marking_db/laser_sources/laser_source_form.html'  # Update with your template path
    success_url = reverse_lazy(
        'pages:laser_source_list')  # Update with your URL name


# Delete view
# The LaserSourceDeleteView class is a view that handles the deletion of a
# LaserSource object.
class LaserSourceDeleteView(DeleteView):
    model = LaserSource
    success_url = reverse_lazy(
        'pages:laser_source_list')  # Update with your URL name


@method_decorator(login_required, name='dispatch')
# The DeleteView class is used to delete an object in a Django application.
class DeleteView(DeleteView):
    model = LaserMarkingParameters
    template_name = 'laser_color_marking_db/laser_markin_parameters/laser_parameters_delete.html'  # Create a template for delete confirmation
    success_url = reverse_lazy(
        'pages:laser_marking_parameters_list')  # Redirect after successful deletion


def search_results(request):
    """
    The `search_results` function takes a POST request, extracts an RGB color
    value from a form, classifies the color using a color spectrum, filters the
    color dictionary, retrieves all colors from a database, classifies each color
    in the database, filters the color dictionary for each color, compares the
    filtered dictionaries, and returns a list of matching colors.

    :param request: The `request` parameter is an object that represents the HTTP
    request made by the user. It contains information such as the request method
    (GET or POST), the submitted form data, the user's IP address, and more. In
    this code, the `request` object is used to access the submitted
    :return: The function `search_results` returns a rendered HTML template based
    on the request method and form validation. If the request method is POST and
    the form is valid, it returns a rendered template with the matching colors. If
    the request method is not POST or the form is not valid, it returns a rendered
    template with the search form.
    """
    form = GaeParamsForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            hex_color = form.cleaned_data['hex_color']
            hex_color = hex_color.lstrip('#')
            rgb_color = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

            if len(rgb_color) != 3:
                return render(request,
                              'laser_color_marking_db/search_logic/search_color.html',
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

            return render(request,
                          'laser_color_marking_db/search_logic/matching_colors.html',
                          {'form': form, 'matching_colors': matching_colors})

    return render(request,
                  'laser_color_marking_db/search_logic/search_color.html',
                  {'form': form})


def home(request):
    """
    The `home` function returns a rendered HTML template for the home page.

    :param request: The request parameter is an object that represents the HTTP
    request made by the client. It contains information such as the HTTP method
    (GET, POST, etc.), headers, user session, and any data sent with the request.
    In this case, it is used to render the 'home.html' template and
    :return: the rendered HTML template 'home.html'.
    """
    return render(request, 'laser_color_marking_db/views/home.html')


def about(request):
    """
    The above function returns a rendered HTML template for the about page.

    :param request: The `request` parameter is an object that represents the HTTP
    request made by the client. It contains information about the request, such as
    the HTTP method (GET, POST, etc.), headers, user session, and any data sent
    with the request. In this code snippet, the `request` object
    :return: the rendered HTML template 'about.html'.
    """
    return render(request, 'laser_color_marking_db/views/about.html')


def contact(request):
    """
    The contact function renders the contact.html template when a request is made.

    :param request: The request parameter is an object that represents the HTTP
    request made by the user. It contains information such as the user's browser,
    IP address, and any data sent with the request
    :return: the rendered HTML template for the contact page.
    """
    return render(request, 'laser_color_marking_db/views/contact.html')


@login_required
def material_list(request):
    """
    The function "material_list" retrieves all materials from the database and
    renders them in a template called "material_list.html".

    :param request: The request parameter is an object that represents the HTTP
    request made by the user. It contains information such as the user's browser,
    IP address, and any data sent with the request
    :return: a rendered HTML template called 'material_list.html' with a context
    variable 'materials' that contains all the Material objects.
    """
    materials = Material.objects.all()
    context = {'materials': materials}
    return render(request,
                  'laser_color_marking_db/materials/material_list.html', context)


@login_required
def laser_source_list(request):
    """
    The function retrieves all laser sources from the database and renders them in
    a template.

    :param request: The `request` parameter is an object that represents the HTTP
    request made by the client. It contains information such as the request
    method, headers, and body. It is typically passed to view functions in Django
    to handle the request and generate a response
    :return: a rendered HTML template called 'laser_source_list.html' with a
    context variable 'laser_sources' that contains all the LaserSource objects.
    """
    laser_sources = LaserSource.objects.all()
    context = {'laser_sources': laser_sources}
    return render(request,
                  'laser_color_marking_db/laser_sources/laser_source_list.html',
                  context)


@login_required
def laser_marking_parameters_list(request):
    """
    The function retrieves all laser marking parameters from the database and
    passes them to the template for rendering.

    :param request: The `request` parameter is an object that represents the HTTP
    request made by the client. It contains information such as the request
    method, headers, user session, and other data related to the request. In this
    code snippet, the `request` parameter is used to render the HTML template and
    pass the
    :return: a rendered HTML template called 'laser_marking_parameters_list.html'
    with a context variable 'laser_marking_parameters' that contains all the
    LaserMarkingParameters objects.
    """
    marking_parameters = LaserMarkingParameters.objects.all()

    context = {'laser_marking_parameters': marking_parameters}
    print(context)
    return render(request,
                  'laser_color_marking_db/laser_markin_parameters/laser_marking_parameters_list.html',
                  context)


from django.shortcuts import render
from django.views.generic import ListView
from .models import LaserMarkingParameters, Material, LaserSource


class LaserParameterListView(LoginRequiredMixin, ListView):
    model = LaserMarkingParameters
    template_name = 'laser_color_marking_db/laser_markin_parameters/laser_marking_parameters_list.html'
    context_object_name = 'laser_marking_parameters'
    ordering = 'id'  # Default ordering

    def get_queryset(self):
        queryset = super().get_queryset()

        # Get filter parameters from request
        material_id = self.request.GET.get('material')
        laser_source_id = self.request.GET.get('laser_source')

        # Apply filters if provided
        if material_id:
            queryset = queryset.filter(material_id=material_id)
        if laser_source_id:
            queryset = queryset.filter(laser_source_id=laser_source_id)

        # Apply ordering
        queryset = queryset.order_by(self.ordering)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add materials and laser sources to the context
        materials = Material.objects.all()
        laser_sources = LaserSource.objects.all()

        context['materials'] = materials
        context['laser_sources'] = laser_sources

        return context


@login_required
def laser_marking_parameters_detail(request, pk):
    """
    The function retrieves laser marking parameters and renders a template with
    the parameters as context.

    :param request: The `request` parameter is an object that represents the HTTP
    request made by the client. It contains information such as the request
    method, headers, user session, and any data sent with the request. In this
    case, it is used to handle the incoming request and render the response
    :param pk: The "pk" parameter stands for "primary key" and is used to identify
    a specific instance of the LaserMarkingParameters model. It is typically used
    to retrieve a specific object from the database based on its primary key value
    :return: a rendered HTML template with the context data.
    """
    marking_parameters = get_object_or_404(LaserMarkingParameters, pk=pk)
    context = {'marking_parameters': marking_parameters}
    return render(request,
                  'laser_color_marking_db/laser_markin_parameters/laser_marking_parameters_detail.html',
                  context)
