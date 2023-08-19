# pages/utils.py

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