from django.contrib import admin

from .models import LaserSource, LaserMarkingParameters, \
    Material

admin.site.register(LaserSource)
admin.site.register(LaserMarkingParameters)

admin.site.register(Material)
