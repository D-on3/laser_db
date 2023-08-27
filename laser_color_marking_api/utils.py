import colorsys

class ColorSpectrum:
    def __init__(self, rgb_values):
        self.rgb_values = rgb_values

    def classify_colors_by_spectrum(self):
        classified_colors = {
            "red": [],
            "orange": [],
            "yellow": [],
            "green": [],
            "blue": [],
            "indigo": [],
            "violet": [],
        }

        for rgb in self.rgb_values:
            h, _, _ = colorsys.rgb_to_hsv(*[val / 255.0 for val in rgb])
            h_degrees = h * 360  # Convert hue to degrees

            if 0 <= h_degrees <= 30:
                classified_colors["red"].append(rgb)
            elif 30 < h_degrees <= 60:
                classified_colors["orange"].append(rgb)
            elif 60 < h_degrees <= 120:
                classified_colors["yellow"].append(rgb)
            elif 120 < h_degrees <= 180:
                classified_colors["green"].append(rgb)
            elif 180 < h_degrees <= 240:
                classified_colors["blue"].append(rgb)
            elif 240 < h_degrees <= 300:
                classified_colors["indigo"].append(rgb)
            elif 300 < h_degrees <= 330:
                classified_colors["violet"].append(rgb)
            else:
                classified_colors["red"].append(rgb)

        return classified_colors

# Example RGB values for rainbow colors
rainbow_rgb_values = [
    (255, 0, 0),      # Red
    (255, 165, 0),    # Orange
    (255, 255, 0),    # Yellow
    (0, 128, 0),      # Green
    (0, 0, 255),      # Blue
    (75, 0, 130),     # Indigo
    (148, 0, 211),    # Violet
    # Add more colors if needed
]

# Create an instance of ColorSpectrum with the rainbow RGB values
rainbow_spectrum = ColorSpectrum(rainbow_rgb_values)

# Classify colors by rainbow spectrum
classified_colors = rainbow_spectrum.classify_colors_by_spectrum()

# Retrieve colors in the "Orange Spectrum"
orange_colors = classified_colors["orange"]

# Print colors in the "Orange Spectrum"
print("Colors in the Orange Spectrum:", orange_colors)

from pages.data_colors_string import data_laserdb
import datetime
from pages.models import LaserSource, LaserMarkingParameters, Material


# ... (Other code remains the same)

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
                'date_published': datetime.datetime.strptime(parts[13],
                                                             '%Y-%m-%d %H:%M:%S'),
                'research_date': datetime.datetime.strptime(parts[14],
                                                            '%Y-%m-%d %H:%M:%S'),
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
            name=laser_source_name, type_of_laser=laser_source_type,
            wavelength=wavelength)

        laser_marking_params = LaserMarkingParameters(
            laser_source=laser_source,
            material=material,
            scanning_speed=entry['scanning_speed'],
            average_power=entry['average_power'],
            scan_step=entry['scan_step'],
            pulse_duration=entry['pulse_duration'],
            pulse_repetition_rate=entry['pulse_repetition_rate'],
            overlap_coefficient=entry['overlap_coefficient'],
            volumetric_density_of_energy=entry[
                'volumetric_density_of_energy'],
            color_red=entry['color_red'],
            color_green=entry['color_green'],
            color_blue=entry['color_blue'],
            author=entry['author'],
            date_published=entry['date_published'],
            research_date=entry['research_date']
        )
        laser_marking_params.save()


if __name__ == "__main__":

    data_list = parse_data_string(data_laserdb)

    populate_database(data_list)