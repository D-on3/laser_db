from django.urls import path
from . import views


app_name = "pages"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('add/', views.add_laser_marking, name='add'),
]