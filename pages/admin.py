from django.contrib import admin

from .models import LaserSource,LaserColorMarking,LaserMarkingParameters,MetalMaterial



admin.register(LaserSource)
admin.register(LaserMarkingParameters)

admin.register(LaserColorMarking)
admin.register(MetalMaterial)
