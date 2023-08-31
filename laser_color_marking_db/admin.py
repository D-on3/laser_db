from django.contrib import admin
from .models import LaserMarkingParameters,LaserSource,Material
# Register your models here.


admin.site.register(LaserMarkingParameters)
admin.site.register(LaserSource)
admin.site.register(Material)

