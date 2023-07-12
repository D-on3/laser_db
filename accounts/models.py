from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional user profile fields as needed
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username