from django.urls import path
from . import views


app_name = "pages"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('add/', views.create_laser_marking_parameters, name='add'),
    path('search/', views.search_laser_sources, name='search_laser_sources'),
    path('laser_sources/', views.laser_source_list, name='laser_source_list'),
    path('laser_sources/<int:laser_source_id>/', views.laser_source_detail, name='laser_source_detail'),
]

