from django.db import models
from django.contrib.auth.models import User
from author.models import Author
from machines.models import Machine
from materials.models import Material
from parameters.models import Parameter

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField()
    accuracy = models.FloatField(null=True, blank=True)
    # Add additional fields related to result information

    def __str__(self):
        return f'Result: {self.id}'