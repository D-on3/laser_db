# api_urls.py

from django.urls import path

from . import views

app_name = 'laser_color_marking_api'


urlpatterns = [
    path('generate-api-key/', views.GenerateAPIKeyView.as_view(), name='generate_api_key'),
    path('laser-sources/', views.LaserSourceList.as_view(), name='laser_source_list'),
    path('laser-sources/<int:pk>/', views.LaserSourceDetail.as_view(), name='laser_source_detail'),
    path('marking-parameters/', views.LaserMarkingParametersList.as_view(), name='marking_parameters_list'),
    path('marking-parameters/<int:pk>/', views.LaserMarkingParametersDetail.as_view(), name='marking_parameters_detail'),
]
