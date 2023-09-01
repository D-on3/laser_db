from django.db import models
from django.utils import timezone
from decimal import Decimal


class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class LaserSource(models.Model):
    name = models.CharField(max_length=100)
    type_of_laser = models.CharField(max_length=100)
    wavelength = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class LaserMarkingParameters(models.Model):
    laser_source = models.ForeignKey(LaserSource, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    scanning_speed = models.PositiveIntegerField()
    average_power = models.DecimalField(max_digits=5, decimal_places=2)
    scan_step = models.FloatField(blank=True, null=True)
    pulse_duration = models.FloatField(blank=True, null=True)
    pulse_repetition_rate = models.PositiveIntegerField(blank=True, null=True)
    overlap_coefficient = models.FloatField(blank=True, null=True)
    volumetric_density_of_energy = models.FloatField(blank=True,
                                                     null=True)  # Made optional
    focus = models.FloatField(blank=True, null=True)
    color_red = models.PositiveIntegerField(blank=True, null=True)
    color_green = models.PositiveIntegerField(blank=True, null=True)
    color_blue = models.PositiveIntegerField(blank=True, null=True)
    authors = models.CharField(max_length=100)
    research_date = models.DateTimeField(default=timezone.now)


    # calculated values
    calculated_volumetric_density_of_energy = models.FloatField(blank=True, null=True)
    calculated_beam_area = models.FloatField(blank=True, null=True)
    calculated_repetition_rate = models.FloatField(blank=True, null=True)
    calculated_brightness = models.FloatField(blank=True, null=True)
    calculated_power_density = models.FloatField(blank=True, null=True)
    calculated_pulse_energy = models.FloatField(blank=True, null=True)
    calculated_volumetric_energy_density = models.FloatField(blank=True, null=True)
    calculated_brightness_color = models.FloatField(blank=True, null=True)
    calculated_intensity = models.FloatField(blank=True, null=True)
    calculated_energy_density = models.FloatField(blank=True, null=True)
    calculated_color_intensity = models.FloatField(blank=True, null=True)

    # ... existing methods ...

    def save(self, *args, **kwargs):
        """
        Override the save method to calculate and assign values to new attributes before saving.
        """


        super().save(*args, **kwargs)



    def __str__(self):
        return f"{self.material} - {self.laser_source}"

    def calculate_volumetric_density_of_energy(self):
        """
        Calculate and return the volumetric energy density using average power and focus.
        """
        """
        Calculate and return the volumetric energy density using average power and focus.
        """
        if self.average_power is not None and self.focus is not None :
            if isinstance(self.average_power, Decimal) and isinstance(
                    self.focus, float):
                if self.focus != 0:
                    try:
                        return self.average_power / Decimal(str(self.focus))
                    except ZeroDivisionError:
                        print(f"Sample name: {self.laser_source} {self.authors} {self.focus}")

        return None

    def calculate_beam_area(self):
        """
        Calculate and return the beam area.
        Beam Area = π * Focus^2
        """
        if self.focus is not None:
            if isinstance(self.focus, float):
                return 3.14159 * self.focus ** 2
        return None

    def calculate_repetition_rate(self):
        """
        Calculate and return the repetition rate.
        Repetition Rate = 1 / Pulse Duration
        """
        if self.pulse_duration is not None:
            if isinstance(self.pulse_duration,
                          float) and self.pulse_duration != 0:
                return 1 / self.pulse_duration
        return None

    def calculate_brightness(self):
        """
        Calculate and return the average brightness of the RGB color values.
        """
        color_values = [self.color_red, self.color_green, self.color_blue]
        valid_color_values = [value for value in color_values if
                              value is not None]
        if valid_color_values:
            return sum(valid_color_values) / len(valid_color_values)
        return None

    def calculate_power_density(self):
        """
        Calculate and return the power density using average power and scan speed.
        """
        if self.average_power is not None and self.scanning_speed is not None:
            if isinstance(self.average_power, Decimal) and isinstance(
                    self.scanning_speed, int):
                return self.average_power / self.scanning_speed
        return None

    def calculate_pulse_energy(self):
        """
        Calculate and return the pulse energy using average power and pulse repetition rate.
        """
        if self.average_power is not None and self.pulse_repetition_rate is not None:
            if isinstance(self.average_power, Decimal) and isinstance(
                    self.pulse_repetition_rate, int):
                return self.average_power / Decimal(
                    str(self.pulse_repetition_rate))
        return None

    def calculate_volumetric_energy_density(self):
        """
        Calculate and return the volumetric energy density using average power and focus.
        """
        if self.average_power is not None and self.focus is not None:
            if isinstance(self.average_power, Decimal) and isinstance(
                    self.focus, float):
                return self.average_power / Decimal(str(self.focus))
        return None

    def calculate_brightness_color(self):
        """
        Calculate and return the overall brightness of the RGB color values.
        """
        color_values = [self.color_red, self.color_green, self.color_blue]
        valid_color_values = [value for value in color_values if
                              value is not None]
        if valid_color_values:
            return sum(valid_color_values) / len(valid_color_values)
        return None

    def calculate_intensity(self):
        """
        Calculate and return the intensity.
        Intensity = Average Power / (π * Focus^2)
        """
        if self.average_power is not None and self.focus is not None:
            if isinstance(self.average_power, float) and isinstance(
                    self.focus, float):
                return self.average_power / (3.14159 * self.focus ** 2)
        return None

    def calculate_energy_density(self):
        """
        Calculate and return the energy density.
        Energy Density (ED) = Pulse Energy / Beam Area
        """
        pulse_energy = self.calculate_pulse_energy()
        beam_area = self.calculate_beam_area()
        if pulse_energy is not None and beam_area is not None and isinstance(
                beam_area, Decimal):
            # This intentionally checks if beam_area is an instance of Decimal instead of float
            return pulse_energy / beam_area
        return None

    def calculate_color_intensity(self):
        """
        Calculate and return the color intensity.
        Color Intensity = Red + Green + Blue
        """
        if self.color_red is not None and self.color_green is not None and self.color_blue is not None:
            if isinstance(self.color_red, int) and isinstance(
                    self.color_green, int) and isinstance(self.color_blue,
                                                          int):
                return self.color_red + self.color_green + self.color_blue
        return None
