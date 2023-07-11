from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_laser_parameter, name='create_laser_parameter'),
    path('edit/<int:laser_parameter_id>', views.edit_laser_parameter, name='edit_laser_parameter'),
    path('delete/<int:laser_parameter_id>', views.delete_laser_parameter, name='delete_laser_parameter'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_view, name='login'),
    path('search/', views.search, name='search'),
]