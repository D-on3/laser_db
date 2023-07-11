from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ColorOutcome(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LaserParameter(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    color_outcome = models.ForeignKey(ColorOutcome, on_delete=models.CASCADE)
    parameter_1 = models.DecimalField(max_digits=10, decimal_places=2)
    parameter_2 = models.DecimalField(max_digits=10, decimal_places=2)
    parameter_3 = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.material} - {self.color_outcome}'
