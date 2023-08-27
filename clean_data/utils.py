
from data_colors_string import data_laserdb
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