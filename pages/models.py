from django.db import models

class MetalMaterial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class LaserSource(models.Model):
    name = models.CharField(max_length=100)
    wavelength = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class LaserMarkingParameters(models.Model):
    laser_source = models.ForeignKey(LaserSource, on_delete=models.CASCADE)
    material = models.ForeignKey(MetalMaterial, on_delete=models.CASCADE)
    scanning_speed = models.PositiveIntegerField()
    average_power = models.DecimalField(max_digits=5, decimal_places=2)
    # Add other fields as needed

    def __str__(self):
        return f"{self.material} - {self.laser_source}"

class LaserColorMarking(models.Model):
    marking_parameters = models.ForeignKey(LaserMarkingParameters, on_delete=models.CASCADE)
    scan_step = models.FloatField()
    pulse_duration = models.FloatField()
    pulse_repetition_rate = models.PositiveIntegerField()
    overlap_coefficient = models.FloatField()
    volumetric_density_of_energy = models.FloatField()
    color_red = models.PositiveIntegerField()
    color_green = models.PositiveIntegerField()
    color_blue = models.PositiveIntegerField()

    def __str__(self):
        return f"Laser Color Marking: {self.marking_parameters.material} - {self.marking_parameters.laser_source}, Color-RGB({self.color_red}, {self.color_green}, {self.color_blue})"
