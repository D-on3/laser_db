from django.contrib import admin
from .models import LaserSource,LaserMarkingParameters,MetalMaterial,LaserColorMarking

# Register your models here.


admin.register(LaserSource)
admin.register(LaserMarkingParameters)
admin.register(MetalMaterial)
admin.register(LaserColorMarking)