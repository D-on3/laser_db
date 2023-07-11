from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields related to the material

    def __str__(self):
        return self.name

class ColorOutcome(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields related to the color outcome

    def __str__(self):
        return self.name

class LaserParameter(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    color_outcome = models.ForeignKey(ColorOutcome, on_delete=models.CASCADE)
    # Add other fields related to the laser parameters

    def __str__(self):
        return f"{self.material} - {self.color_outcome}"