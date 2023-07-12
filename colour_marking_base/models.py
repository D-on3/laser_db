from django.db import models
from django.contrib.auth.models import User

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ColorOutcome(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Machine(models.Model):
    manufacturer = models.CharField(max_length=100)
    model_machine = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.manufacturer + ' ' + self.model_machine

class Results(models.Model):
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
