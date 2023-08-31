# laser_optimization/views.py
from django.shortcuts import render
from laser_color_marking_db.models import LaserMarkingParameters, Material, LaserSource
from laser_cm_optimisation.optimization import optimize_parameters


def optimize_parameters_view(request):
    materials = Material.objects.all()
    laser_sources = LaserSource.objects.all()

    optimized_parameters = {}

    if request.method == 'POST':
        material_id = int(request.POST['material'])
        laser_source_id = int(request.POST['laser_source'])
        material = Material.objects.get(pk=material_id)
        laser_source = LaserSource.objects.get(pk=laser_source_id)
        optimized_parameters = optimize_parameters(material, laser_source)

    return render(request, 'laser_cm_optimisations/optimise_parameters.html', {
        'materials': materials,
        'laser_sources': laser_sources,
        'optimized_parameters': optimized_parameters,
    })


from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def plot_view(request):
    # Define the objective function to visualize
    def objective_function(x):
        return x[0]**2 + x[1]**2

    # Create a grid of parameter values
    x_range = np.linspace(-2, 2, 100)
    y_range = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x_range, y_range)
    Z = objective_function([X, Y])

    # Create a contour plot
    plt.contourf(X, Y, Z, levels=20, cmap='viridis')
    plt.colorbar(label='Objective Function Value')
    plt.xlabel('Parameter 1')
    plt.ylabel('Parameter 2')
    plt.title('Contour Plot of Objective Function')

    # Convert plot to image and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_image = base64.b64encode(buffer.read()).decode()

    plt.close()  # Clear the plot

    return render(request, 'laser_cm_optimisations/plot_template.html', {'plot_image': plot_image})

