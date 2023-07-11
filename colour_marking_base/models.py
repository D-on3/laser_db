from django.db import models
from django.contrib.auth.models import User

class LaserMaterial(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LaserColor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LaserParameter(models.Model):
    material = models.ForeignKey(LaserMaterial, on_delete=models.CASCADE)
    color = models.ForeignKey(LaserColor, on_delete=models.CASCADE)
    power = models.FloatField()
    pulse_duration = models.FloatField()
    repetition_rate = models.FloatField()
    focus_position = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.material} - {self.color}'
