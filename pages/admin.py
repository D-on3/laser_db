from django.contrib import admin
from .models import LaserSource,LaserColorMarking,LaserMarkingParameters,MetalMaterial
# Register your models here.


admin.register(LaserSource)
admin.register(LaserMarkingParameters)
admin.register(LaserColorMarking)
admin.register(MetalMaterial)
