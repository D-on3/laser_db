from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.material_list, name='materials_list'),
]
