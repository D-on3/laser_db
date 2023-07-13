from django.db import models
from django.contrib.auth.models import User
from author.models import Author
from machines.models import Machine
from materials.models import Material

from colors.models import Color
from author.models import Author
class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    power = models.FloatField()
    pulse_duration = models.FloatField()
    repetition_rate = models.FloatField()
    focus_position = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField()
    accuracy = models.FloatField(null=True, blank=True)
    # Add additional fields related to result information

    def __str__(self):
        return f'Result: {self.id}'