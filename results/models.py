from django.db import models
from django.contrib.auth.models import User
from author.models import Author
from machines.models import Machine
from materials.models import Material
from colors.models import ColorOutcome

class Result(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    color = models.ForeignKey(ColorOutcome, on_delete=models.CASCADE)
    power = models.FloatField()
    pulse_duration = models.FloatField()
    repetition_rate = models.FloatField()
    focus_position = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.material} - {self.color}'
