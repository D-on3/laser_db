from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    url = models.URLField(blank=True)
    institution = models.CharField(max_length=100)
    # Add additional fields related to the author's work

    def __str__(self):
        return self.name