from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.machine_list, name='machine_list'),
]
