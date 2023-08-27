from django.urls import path
from . import views

app_name = "pages"
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('create_machine/', views.create_machine, name='create_machine'),
    path('create_parameters/', views.create_laser_marking_parameters,
         name='create_parameters'),

    path('laser_source_list/', views.laser_source_list,
         name='laser_source_list'),
    path('laser_source_detail/<int:pk>/', views.laser_source_detail,
         name='laser_source_detail'),
    path('create_laser_source/', views.create_laser_source,
         name='create_laser_source'),
    path('update_laser_source/<int:pk>/', views.update_laser_source,
         name='update_laser_source'),
    path('delete_laser_source/<int:pk>/', views.delete_laser_source,
         name='delete_laser_source'),

    path('laser_marking_parameters_list/',
         views.laser_marking_parameters_list,
         name='laser_marking_parameters_list'),
    path('laser_marking_parameters_detail/<int:pk>/',
         views.laser_marking_parameters_detail,
         name='laser_marking_parameters_detail'),
    path('create_laser_marking_parameters/',
         views.create_laser_marking_parameters,
         name='create_laser_marking_parameters'),
    path('update_laser_marking_parameters/<int:pk>/',
         views.update_laser_marking_parameters,
         name='update_laser_marking_parameters'),
    path('delete_laser_marking_parameters/<int:pk>/',
         views.delete_laser_marking_parameters,
         name='delete_laser_marking_parameters'),
    path('search_by_color/', views.search_by_color, name='search_by_color'),
]
