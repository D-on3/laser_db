from django.db import models

class Machine(models.Model):
    manufacturer = models.CharField(max_length=100)
    model_machine = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.manufacturer} {self.model_machine}'
