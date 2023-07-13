from django.db import models

class Machine(models.Model):
    manufacturer = models.CharField(max_length=100)
    model_machine = models.CharField(max_length=100)
    machine_type = models.CharField(max_length=100)
    machine_link = models.URLField(blank=True)
    # Add additional fields related to machine information

    def __str__(self):
        return f'{self.manufacturer} {self.model_machine}'
