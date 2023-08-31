# laser_optimization/urls.py
from django.urls import path
from . import views

app_name = 'laser_cm_optimisation'

urlpatterns = [
    path('', views.optimize_parameters_view, name='optimize_parameters'),
    path('plot/', views.plot_view, name='plot'),

]