from django.db import models
from django.utils import timezone


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
    scan_step = models.FloatField()
    pulse_duration = models.FloatField()
    pulse_repetition_rate = models.PositiveIntegerField()
    overlap_coefficient = models.FloatField()
    volumetric_density_of_energy = models.FloatField()

    # Color channels
    color_red = models.PositiveIntegerField()
    color_green = models.PositiveIntegerField()
    color_blue = models.PositiveIntegerField()

    # Additional fields
    author = models.CharField(max_length=100)
    date_published = models.DateTimeField(
        default=timezone.now)  # Default to current date
    research_date = models.DateTimeField(
        default=timezone.now)  # Default to current date

    def __str__(self):
        return f"{self.material} - {self.laser_source}"
