from django.urls import path
from . import views

app_name = 'announcements'

urlpatterns = [
    path('', views.announcement_list_view, name='announcement_list'),
    path('<int:pk>/', views.announcement_detail_view, name='announcement_detail'),
]
