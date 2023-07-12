from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.result_create, name='result_create'),
    path('list/', views.result_list, name='result_list'),
]
