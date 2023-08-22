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
