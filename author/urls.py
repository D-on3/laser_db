from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.author_list, name='author_list'),
]
