from django.db import models
from django.contrib.auth.models import User

class Color(models.Model):
    name = models.CharField(max_length=100)
    hex_code = models.CharField(max_length=7)
    rgb_values = models.CharField(max_length=15)
    image = models.ImageField(upload_to='colors/', blank=True, null=True)
    # Add additional fields related to color information

    def __str__(self):
        return self.name