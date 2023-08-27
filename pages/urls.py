from django.urls import path
from . import views

app_name = "pages"
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('materials/', views.material_list, name='material_list'),
    path('laser-sources/', views.laser_source_list, name='laser_source_list'),
    path('laser-marking-parameters/', views.laser_marking_parameters_list,
         name='laser_marking_parameters_list'),
]
