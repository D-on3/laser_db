from django.urls import path
from .views import *

app_name = "laser_color_marking_db"
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('materials/', material_list, name='material_list'),
    path('laser-sources/', laser_source_list, name='laser_source_list'),
    path('laser-marking-parameters/', LaserParameterListView.as_view(),
         name='laser_marking_parameters_list'),
    # Add the following line for the details view
    path('laser-marking-parameters/<int:pk>/',
         laser_marking_parameters_detail,
         name='laser_marking_parameters_detail'),
    path('update/<int:pk>/', UpdateView.as_view(), name='update_view'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete_view'),
    path('search/', search_results, name='search_colors'),
    path('add_sample/', add_sample, name='add_sample'),
    path('add_laser_source/', add_laser_source, name='add_laser_source'),
    path('add_material/', add_material, name='add_material'),
    path('material/<int:pk>/update/', update_material,
         name='update_material'),
    path('material/<int:pk>/delete/', delete_material,
         name='delete_material'),
    path('laser_sources/', laser_source_list, name='laser_source_list'),
    # path('laser_sources/<int:pk>/update/',
    #      LaserSourceUpdateView.as_view(), name='update_laser_source'),
    path('laser_sources/<int:pk>/delete/',
         LaserSourceDeleteView.as_view(), name='delete_laser_source'),
    path('run-util-code/', run_util_code_view, name='run_util_code'),
]
