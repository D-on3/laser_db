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
    laser_source = models.ForeignKey(LaserSource,
                                     on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    scanning_speed = models.PositiveIntegerField()
    average_power = models.DecimalField(max_digits=5, decimal_places=2)
    scan_step = models.FloatField(blank=True, null=True)
    pulse_duration = models.FloatField(blank=True, null=True)
    pulse_repetition_rate = models.PositiveIntegerField(blank=True,
                                                        null=True)
    overlap_coefficient = models.FloatField(blank=True, null=True)
    volumetric_density_of_energy = models.FloatField(blank=True,
                                                     null=True)  # Made optional
    focus = models.FloatField(blank=True, null=True)
    color_red = models.PositiveIntegerField(blank=True, null=True)
    color_green = models.PositiveIntegerField(blank=True, null=True)
    color_blue = models.PositiveIntegerField(blank=True, null=True)
    authors = models.CharField(max_length=100)
    research_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.authors