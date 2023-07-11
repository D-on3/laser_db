from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('export/', views.export_laser_parameters, name='export_laser_parameters'),
    # ...
]