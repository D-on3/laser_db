from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.name