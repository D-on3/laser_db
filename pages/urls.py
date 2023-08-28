from django.urls import path
from . import views
from .views import *

app_name = "pages"
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('materials/', views.material_list, name='material_list'),
    path('laser-sources/', views.laser_source_list, name='laser_source_list'),
    path('laser-marking-parameters/', views.laser_marking_parameters_list,
         name='laser_marking_parameters_list'),
    # Add the following line for the details view
    path('laser-marking-parameters/<int:pk>/',
         views.laser_marking_parameters_detail,
         name='laser_marking_parameters_detail'),
    path('update/<int:pk>/', UpdateView.as_view(), name='update_view'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete_view'),
    path('search/', views.search_results, name='search_colors'),
]
