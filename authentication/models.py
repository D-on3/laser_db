from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class UserProfile(AbstractBaseUser):
    username = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='avatars/', blank=True)
    bio = models.TextField(blank=True)
    api_token = models.CharField(max_length=40, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    # Other fields and methods...

    def __str__(self):
        return self.email
