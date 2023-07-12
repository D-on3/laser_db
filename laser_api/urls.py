from django.urls import path
from . import views

app_name = 'results'

urlpatterns = [
    path('materials/', views.MaterialListAPIView.as_view(),
         name='material-list'),
    path('api/materials/<int:pk>/', views.MaterialDetailAPIView.as_view(),
         name='material-detail'),
    path('authors/', views.AuthorListAPIView.as_view(),
         name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetailAPIView.as_view(),
         name='author-detail'),
    path('machines/', views.MachineListAPIView.as_view(),
         name='machine-list'),
    path('machines/<int:pk>/', views.MachineDetailAPIView.as_view(),
         name='machine-detail'),
    path('colors/', views.ColorOutcomeListAPIView.as_view(),
         name='color-list'),
    path('colors/<int:pk>/', views.ColorOutcomeDetailAPIView.as_view(),
         name='color-detail'),
]
