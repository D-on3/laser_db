# pages/utils.py

import colorsys
from django.utils import timezone
from laser_db.pages.models import LaserMarkingParameters, Material, LaserSource
import datetime
import os
import django



# Now you can import your models
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Rest of your script...

def rgb_to_hex(red, green, blue):
    """
    Convert RGB color values to hexadecimal format.
    :param red: Red color value (0-255)
    :param green: Green color value (0-255)
    :param blue: Blue color value (0-255)
    :return: Hexadecimal color string (e.g., '#RRGGBB')
    """
    hex_color = "#{:02X}{:02X}{:02X}".format(red, green, blue)
    return hex_color

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
            h_degrees = h * 360

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


    def __str__(self):
        return f"{self.classified_colors}"


def get_value(value):
    if value == '-':
        return None
    elif value.isdigit():
        return int(value)
    elif '.' in value:
        return float(value)
    else:
        return value.strip('"')
def get_author(value):
    return value
def parse_data_string(data_string):
    data_list = []
    lines = data_string.strip().split('\n')
    for line in lines:
        parts = line.split(',')

        # Unpack values using indexing
        color_red = get_value(parts[0])
        color_green = get_value(parts[1])
        color_blue = get_value(parts[2])
        material_name = get_value(parts[3])
        laser_type_name = get_value(parts[4])
        wavelength = get_value(parts[5])
        scanning_speed = get_value(parts[6])
        average_power = get_value(parts[7])
        scan_step = get_value(parts[8])
        pulse_duration = get_value(parts[9])
        pulse_repetition_rate = get_value(parts[10])
        focus = get_value(parts[11])
        authors = get_author(parts[12])
        research_date = get_value(parts[13])

        research_date = timezone.make_aware(
            timezone.datetime.strptime(research_date, "%Y"),
            timezone.get_current_timezone()
        )

        laser_source_obj, _ = LaserSource.objects.get_or_create(
            name=laser_type_name,
            type_of_laser=laser_type_name,
            wavelength=int(wavelength)
        )

        material_obj, _ = Material.objects.get_or_create(name=material_name)
        print((timezone.datetime.strptime(str(research_date),"%Y-%m-%d %H:%M:%S%z")))
        laser_parameters = LaserMarkingParameters(
            # The above code is assigning the value of the variable
            # "laser_source_obj" to the variable "laser_source".
            laser_source=laser_source_obj,
            material=material_obj,
            scanning_speed=scanning_speed,
            average_power=average_power,
            scan_step=scan_step,
            pulse_duration=pulse_duration,
            pulse_repetition_rate=pulse_repetition_rate,
            focus=focus,
            authors=authors,
            research_date=timezone.datetime.strptime(str(research_date), "%Y-%m-%d %H:%M:%S%z")
        )


        # Set color values
        laser_parameters.color_red = color_red
        laser_parameters.color_green = color_green
        laser_parameters.color_blue = color_blue

        # Append the parameters to data_list
        data_list.append(laser_parameters)

    return data_list

if __name__ == "__main__":

    # Set the DJANGO_SETTINGS_MODULE environment variable
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "laser_db.settings")  # Replace "your_project_name" with the actual project name

    # Initialize Django
    django.setup()

    data_laserdb = '''
54,30,104,Ti, Nd-YAG,1064,550,20,10,80,200,2,"E. Sprudzs-A. Blums-J. Aulins","2021"
99,57,133,AISI_304, UV,355,400,7.1,30,40,25,-3,"Y. Liu-H. Zheng-Z. Li","2020"
131,76,131,AISI_304, Fiber,1064,60,18,50,85,112,0,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013"
175,133,157,AISI_304, Fiber,1064,132,4.4,-,80,230,0,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013"
214,171,199,AISI_304, Fiber,1062,150,5,10,80,100,0,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013"
251,165,255,Ti, Nd-YAG,1064,260,53,-,-,-,0,"A. V. Kabashin-P. M. Bolshakov-A. V. Terekhov","2003"
112,89,231,Ti, Fiber,1064,60,30,-,35,200,2,"M. W. Ahmed-A. Batool-S. A. Ansari-M. Iqbal","2020"
124,173,250,Ti, Nd-YAG,1064,240,53,-,-,-,-,"A. V. Kabashin-P. M. Bolshakov-A. V. Terekhov","2003"
98,186,236,AISI_304, Fiber,1064,100,6,-,20,100,-,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013"
153,201,250,AISI_304, Fiber,1062,125,3.1,10,80,100,-,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013"
111,163,184,AISI_304, Fiber,1064,100,4.4,-,80,230,-,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013"
119,149,173,AISI_304, Fiber,1064,130,18,30,85,112,-,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013"
88,123,177,Ti, Nd-YAG,1064,450,20,10,80,200,2,"E. Sprudzs-A. Blums-J. Aulins","2021"
5,121,136,AISI_304, UV,355,400,7,30,40,25,3,"Y. Liu-H. Zheng-Z. Li","2020"
6,123,140,AISI_304, Fiber,1064,60,6,50,70,100,0,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013"
25,170,139,AISI_304, UV,355,400,7,30,40,25,3,"Y. Liu-H. Zheng-Z. Li","2020"
98,231,236,Ti, Fiber,1064,80,30,-,35,200,2,"M. W. Ahmed-A. Batool-S. A. Ansari-M. Iqbal","2020"
135,227,212,AISI_304, Fiber,1062,75,3.2,10,80,100,-,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013"
146,238,201,AISI_304, Fiber,1064,500,10,-,40,100,-,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013"
193,215,114,AISI_304, Fiber,1064,80,18,50,85,112,-,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013"
252,251,142,Ti, Nd-YAG,1064,350,53,-,-,-,-,"A. V. Kabashin-P. M. Bolshakov-A. V. Terekhov","2003"
245,244,138,AISI_304, Fiber,1064,10,2,-,40,100,-,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013"
248,241,134,Ti, Fiber,1064,130,30,-,35,200,-,"M. W. Ahmed-A. Batool-S. A. Ansari-M. Iqbal","2020"
251,235,199,AISI_304, Fiber,1064,400,4.4,-,80,230,-,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013"
250,218,143,AISI_304, Fiber,1062,150,3,10,80,100,-,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013"
241,169,169,AISI_304, Fiber,1062,130,4,10,80,100,-,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013"
250,148,130,AISI_304, Fiber,1070,10,5,50,90,100,-,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013"
168,149,91,AISI_304, Fiber,1062,50,8,10,80,100,-,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013"
182,159,47,AISI_304, Fiber,1064,50,4.4,-,80,230,-,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013"
243,159,82,AISI_304, Fiber,1070,150,9,50,30,100,0,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013"
211,138,10,AISI_304, Fiber,1064,100,6,-,20,100,-,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013"
206,140,54,Ti, Fiber,1064,60,19.5,-,35,200,2,"M. W. Ahmed-A. Batool-S. A. Ansari-M. Iqbal","2020"
181,127,31,Ti, Nd-YAG,1064,100,53,-,-,-,-,"A. V. Kabashin-P. M. Bolshakov-A. V. Terekhov","2003"
183,120,7,AISI_304, Fiber,1064,80,18,50,85,112,0,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013"
169,119,60,Ti, Nd-YAG,1064,850,20,10,80,200,2,"E. Sprudzs-A. Blums-J. Aulins","2021"
115,61,14,AISI_304, UV,355,400,8,30,40,25,3,"Y. Liu-H. Zheng-Z. Li","2020"

'''
    second_data = '''
54,30,104,Ti, Nd-YAG,1064,550,20,10,80,200,2,"E. Sprudzs-A. Blums-J. Aulins","2021","Influence of power density and frequency of the process of laser marking of steel products"
99,57,133,AISI 304, UV,355,400,7.1,30,40,25,-3,"Y. Liu-H. Zheng-Z. Li","2020","Analyzing the effect of the parameters of laser etching process influencing the corrosion resistance and surface roughness of marine grade 316 stainless steel"
131,76,131,AISI 304, Fiber,1064,60,18,50,85,112,0,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013","Modeling of laser-colored stainless steel surfaces by color pixels"
175,133,157,AISI 304, Fiber,1064,132,4.4,-,80,230,0,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
214,171,199,AISI 304, Fiber,1062,150,5,10,80,100,0,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
251,165,255,Ti, Nd-YAG,1064,260,53,-,-,-,0,"A. V. Kabashin-P. M. Bolshakov-A. V. Terekhov","2003","Analysis of oxide formation induced by UV laser coloration of stainless steel"
112,89,231,Ti, Fiber,1064,60,30,-,35,200,2,"M. W. Ahmed-A. Batool-S. A. Ansari-M. Iqbal","2020","Colorizing of the stainless steel surface by single-beam direct femtosecond laser writing"
124,173,250,Ti, Nd-YAG,1064,240,53,-,-,-,-,"A. V. Kabashin-P. M. Bolshakov-A. V. Terekhov","2003","Analysis of oxide formation induced by UV laser coloration of stainless steel"
98,186,236,AISI 304, Fiber,1064,100,6,-,20,100,-,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
153,201,250,AISI 304, Fiber,1062,125,3.1,10,80,100,-,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
111,163,184,AISI 304, Fiber,1064,100,4.4,-,80,230,-,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
119,149,173,AISI 304, Fiber,1064,130,18,30,85,112,-,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
88,123,177,Ti, Nd-YAG,1064,450,20,10,80,200,2,"E. Sprudzs-A. Blums-J. Aulins","2021","Influence of power density and frequency of the process of laser marking of steel products"
5,121,136,AISI 304, UV,355,400,7,30,40,25,3,"Y. Liu-H. Zheng-Z. Li","2020","Analyzing the effect of the parameters of laser etching process influencing the corrosion resistance and surface roughness of marine grade 316 stainless steel"
6,123,140,AISI 304, Fiber,1064,60,6,50,70,100,0,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
25,170,139,AISI 304, UV,355,400,7,30,40,25,3,"Y. Liu-H. Zheng-Z. Li","2020","Analyzing the effect of the parameters of laser etching process influencing the corrosion resistance and surface roughness of marine grade 316 stainless steel"
98,231,236,Ti, Fiber,1064,80,30,-,35,200,2,"M. W. Ahmed-A. Batool-S. A. Ansari-M. Iqbal","2020","Colorizing of the stainless steel surface by single-beam direct femtosecond laser writing"
135,227,212,AISI 304, Fiber,1062,75,3.2,10,80,100,-,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
146,238,201,AISI 304, Fiber,1064,500,10,-,40,100,-,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
193,215,114,AISI 304, Fiber,1064,80,18,50,85,112,-,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
252,251,142,Ti, Nd-YAG,1064,350,53,-,-,-,-,"A. V. Kabashin-P. M. Bolshakov-A. V. Terekhov","2003","Analysis of oxide formation induced by UV laser coloration of stainless steel"
245,244,138,AISI 304, Fiber,1064,10,2,-,40,100,-,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
248,241,134,Ti, Fiber,1064,130,30,-,35,200,-,"M. W. Ahmed-A. Batool-S. A. Ansari-M. Iqbal","2020","Colorizing of the stainless steel surface by single-beam direct femtosecond laser writing"
251,235,199,AISI 304, Fiber,1064,400,4.4,-,80,230,-,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
250,218,143,AISI 304, Fiber,1062,150,3,10,80,100,-,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
241,169,169,AISI 304, Fiber,1062,130,4,10,80,100,-,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
250,148,130,AISI 304, Fiber,1070,10,5,50,90,100,-,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
168,149,91,AISI 304, Fiber,1062,50,8,10,80,100,-,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
182,159,47,AISI 304, Fiber,1064,50,4.4,-,80,230,-,"A. Antonczak-D. Kocon-M. Nowak-P. Kozioł-K. Abramski","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
243,159,82,AISI 304, Fiber,1070,150,9,50,30,100,0,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
211,138,10,AISI 304, Fiber,1064,100,6,-,20,100,-,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
206,140,54,Ti, Fiber,1064,60,19.5,-,35,200,2,"M. W. Ahmed-A. Batool-S. A. Ansari-M. Iqbal","2020","Colorizing of the stainless steel surface by single-beam direct femtosecond laser writing"
181,127,31,Ti, Nd-YAG,1064,100,53,-,-,-,-,"A. V. Kabashin-P. M. Bolshakov-A. V. Terekhov","2003","Analysis of oxide formation induced by UV laser coloration of stainless steel"
183,120,7,AISI 304, Fiber,1064,80,18,50,85,112,0,"M. Kuittinen-A. Lehmuskero-J. Hiltunen","2013","Laser-induced colour marking—Sensitivity scaling for a stainless steel"
169,119,60,Ti, Nd-YAG,1064,850,20,10,80,200,2,"E. Sprudzs-A. Blums-J. Aulins","2021","Influence of power density and frequency of the process of laser marking of steel products"
115,61,14,AISI 304, UV,355,400,8,30,40,25,3,"Y. Liu-H. Zheng-Z. Li","2020","Analyzing the effect of the parameters of laser etching process influencing the corrosion resistance and surface roughness of marine grade 316 stainless steel"
'''

    # Print the data

    data_list = parse_data_string(data_laserdb)


    # Save data to the database
    for parameters in data_list:
        parameters.save()

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
