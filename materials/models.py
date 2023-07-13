from django.db import models


class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    properties = models.TextField()
    msds_link = models.URLField(blank=True)
    # Add additional fields related to material information

    def __str__(self):
        return self.name