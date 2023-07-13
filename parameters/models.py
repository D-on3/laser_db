from django.db import models
from accounts.models import User
from colors.models import Color
from materials.models import Material
from machines.models import Machine

class Parameter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    power = models.FloatField()
    pulse_duration = models.FloatField()
    repetition_rate = models.FloatField()
    focus_position = models.FloatField()
    # Add additional fields related to parameters if needed

    def __str__(self):
        return f'Parameter: {self.id}'