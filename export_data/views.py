import csv
from django.http import HttpResponse

def export_laser_parameters(request):
    laser_parameters = LaserParameter.objects.all()

    # Generate the export file in CSV format
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="laser_parameters.csv"'

    writer = csv.writer(response)
    writer.writerow(['Material', 'Color Outcome', 'Parameter 1', 'Parameter 2', 'Parameter 3'])
    for parameter in laser_parameters:
        writer.writerow([
            parameter.material,
            parameter.color_outcome,
            parameter.parameter_1,
            parameter.parameter_2,
            parameter.parameter_3,
        ])

    return response