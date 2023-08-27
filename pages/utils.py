# pages/utils.py

import colorsys

import datetime
import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laser_db.settings")  # Replace "your_project_name" with the actual project name

# Initialize Django
django.setup()

# Now you can import your models
from pages.models import LaserSource, LaserMarkingParameters, Material

# Rest of your script...

def hex_to_rgb(red, green, blue):
    """
    Convert RGB color values to hexadecimal format.
    :param red: Red color value (0-255)
    :param green: Green color value (0-255)
    :param blue: Blue color value (0-255)
    :return: Hexadecimal color string (e.g., '#RRGGBB')
    """
    hex_color = "#{:02X}{:02X}{:02X}".format(red, green, blue)
    return hex_color


# class ColorSpectrum:
#     def __init__(self, rgb_values):
#         self.rgb_values = rgb_values
#
#     def classify_colors_by_spectrum(self):
#         classified_colors = {
#             "red": [],
#             "orange": [],
#             "yellow": [],
#             "green": [],
#             "blue": [],
#             "indigo": [],
#             "violet": [],
#         }
#
#         for rgb in self.rgb_values:
#             h, _, _ = colorsys.rgb_to_hsv(*[val / 255.0 for val in rgb])
#             h_degrees = h * 360  # Convert hue to degrees
#
#             if 0 <= h_degrees <= 30:
#                 classified_colors["red"].append(rgb)
#             elif 30 < h_degrees <= 60:
#                 classified_colors["orange"].append(rgb)
#             elif 60 < h_degrees <= 120:
#                 classified_colors["yellow"].append(rgb)
#             elif 120 < h_degrees <= 180:
#                 classified_colors["green"].append(rgb)
#             elif 180 < h_degrees <= 240:
#                 classified_colors["blue"].append(rgb)
#             elif 240 < h_degrees <= 300:
#                 classified_colors["indigo"].append(rgb)
#             elif 300 < h_degrees <= 330:
#                 classified_colors["violet"].append(rgb)
#             else:
#                 classified_colors["red"].append(rgb)
#
#         return classified_colors
#
#
#



import datetime
from django.utils import timezone
from pages.models import LaserSource, LaserMarkingParameters, Material

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None

def parse_data_string(data_string):
    data_lines = data_string.strip().split('\n')
    data = []

    for line in data_lines:
        parts = line.split(',')
        if len(parts) == 15:
            entry = {
                'color_red': convert_to_int(parts[0]),
                'color_green': convert_to_int(parts[1]),
                'color_blue': convert_to_int(parts[2]),
                'laser_source': parts[3],
                'wavelength': convert_to_int(parts[4]),
                'scanning_speed': convert_to_int(parts[5]),
                'average_power': convert_to_float(parts[6]),
                'scan_step': convert_to_float(parts[7]),
                'pulse_duration': convert_to_float(parts[8]),
                'pulse_repetition_rate': convert_to_int(parts[9]),
                'overlap_coefficient': convert_to_float(parts[10]),
                'volumetric_density_of_energy': convert_to_float(parts[11]),
                'author': parts[12],
                'date_published': timezone.make_aware(datetime.datetime.strptime(parts[13], '%Y-%m-%d %H:%M:%S')),
                'research_date': timezone.make_aware(datetime.datetime.strptime(parts[14], '%Y-%m-%d %H:%M:%S')),
            }
            data.append(entry)
        else:
            print(f"Skipping malformed line: {line}")

    return data

def populate_database(data_list):
    for entry in data_list:
        material_name = entry['laser_source']
        material, _ = Material.objects.get_or_create(name=material_name)

        laser_source_name = entry['laser_source']
        laser_source_type = entry['laser_source']
        wavelength = entry['wavelength']
        laser_source, _ = LaserSource.objects.get_or_create(
            name=laser_source_name, type_of_laser=laser_source_type, wavelength=wavelength)

        laser_marking_params = LaserMarkingParameters(
            laser_source=laser_source,
            material=material,
            scanning_speed=entry['scanning_speed'] or 0,
            average_power=entry['average_power'] or 0.0,
            scan_step=entry['scan_step'] or 0.0,
            pulse_duration=entry['pulse_duration'] or 0.0,
            pulse_repetition_rate=entry['pulse_repetition_rate'] or 0,
            overlap_coefficient=entry['overlap_coefficient'] or 0.0,
            volumetric_density_of_energy=entry['volumetric_density_of_energy'] or 0.0,
            color_red=entry['color_red'] or 0,
            color_green=entry['color_green'] or 0,
            color_blue=entry['color_blue'] or 0,
            author=entry['author'],
            date_published=entry['date_published'],
            research_date=entry['research_date']
        )
        laser_marking_params.save()

if __name__ == "__main__":
    data_laserdb = '''
    54,30,104,Ti Nd-YAG,1064,550,20,10,80,200,2,23,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    99,57,133,AISI 304,355,400,7.1,30,40,25,-3,3.5,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    131,76,131,AISI 304,1064,60,18,50,85,112,0,14,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    175,133,157,AISI 304,1064,132,4.4,-,80,230,0,15,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    214,171,199,AISI 304,1062,150,5,10,80,100,0,6,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    251,165,255,Ti Nd-YAG,1064,260,53,-,-,-,0,20,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    112,89,231,Ti Fiber,1064,60,30,-,35,200,2,16,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    124,173,250,Ti Nd-YAG,1064,240,53,-,-,-,-,20,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    98,186,236,AISI 304,1064,100,6,-,20,100,-,19,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    153,201,250,AISI 304,1062,125,3.1,10,80,100,-,6,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    111,163,184,AISI 304,1064,100,4.4,-,80,230,-,15,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    119,149,173,AISI 304,1064,130,18,30,85,112,-,14,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    88,123,177,Ti Nd-YAG,1064,450,20,10,80,200,2,23,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    5,121,136,AISI 304,355,400,7,30,40,25,3,3,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    6,123,140,AISI 304,1064,60,6,50,70,100,0,18,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    25,170,139,AISI 304,355,400,7,30,40,25,3.2,3,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    98,231,236,Ti Fiber,1064,80,30,-,35,200,2,16,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    135,227,212,AISI 304,1062,75,3.2,10,80,100,-,6,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    146,238,201,AISI 304,1064,500,10,-,40,100,-,19,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    193,215,114,AISI 304,1064,80,18,50,85,112,-,14,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    252,251,142,Ti Nd-YAG,1064,350,53,-,-,-,-,20,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    245,244,138,AISI 304,1064,10,2,-,40,100,-,19,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    248,241,134,Ti Fiber,1064,130,30,-,35,200,-,16,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    251,235,199,AISI 304,1064,400,4.4,-,80,230,-,15,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    250,218,143,AISI 304,1062,150,3,10,80,100,-,6,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    241,169,169,AISI 304,1062,130,4,10,80,100,-,6,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    250,148,130,AISI 304,1070,10,5,50,90,100,-,18,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    168,149,91,AISI 304,1062,50,8,10,80,100,-,6,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    182,159,47,AISI 304,1064,50,4.4,-,80,230,-,15,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    243,159,82,AISI 304,1070,150,9,50,30,100,0,18,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    211,138,10,AISI 304,1064,100,6,-,20,100,-,19,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    206,140,54,Ti Fiber,1064,60,19.5,-,35,200,2,16,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    181,127,31,Ti Nd-YAG,1064,100,53,-,-,-,-,20,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    183,120,7,AISI 304,1064,80,18,50,85,112,0,14,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    169,119,60,Ti Nd-YAG,1064,850,20,10,80,200,2,23,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    115,61,14,AISI 304,355,400,8,30,40,25,3,Author Name,2023-08-27 12:34:56,2023-08-27 12:34:56
    '''

    data_list = parse_data_string(data_laserdb)
    populate_database(data_list)

    #
    # # Example RGB values for rainbow colors
    # rainbow_rgb_values = [
    #     (255, 0, 0),  # Red
    #     (255, 165, 0),  # Orange
    #     (255, 255, 0),  # Yellow
    #     (0, 128, 0),  # Green
    #     (0, 0, 255),  # Blue
    #     (75, 0, 130),  # Indigo
    #     (148, 0, 211),  # Violet
    #     # Add more colors if needed
    # ]
    #
    # # Create an instance of ColorSpectrum with the rainbow RGB values
    # rainbow_spectrum = ColorSpectrum(rainbow_rgb_values)
    #
    # # Classify colors by rainbow spectrum
    # classified_colors = rainbow_spectrum.classify_colors_by_spectrum()
    #
    # # Retrieve colors in the "Orange Spectrum"
    # orange_colors = classified_colors["orange"]
    #
    # # Print colors in the "Orange Spectrum"
    # print("Colors in the Orange Spectrum:", orange_colors)
