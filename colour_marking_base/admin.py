from django.contrib import admin
from .models import Material,ColorOutcome, LaserParameter
# Register your models here.

admin.register(Material)
admin.register(ColorOutcome)
admin.register(LaserParameter)