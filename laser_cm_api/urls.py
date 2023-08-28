# your_app/urls.py

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

app_name = "laser_cm_api"
urlpatterns = [
    # ...
    # path('token/', TokenObtainPairView.as_view(),
    #      name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(),
    #      name='token_refresh'),
    path('marking-parameters/', LaserMarkingParametersList.as_view(),
         name='marking-parameters-list'),
    path('marking-parameters/<int:pk>/',
         LaserMarkingParametersDetail.as_view(),
         name='marking-parameters-detail'),
    path('search-color/', ColorSearchAPIView.as_view(),
         name='color-search-api'),
    path('docs/', landing_page, name='docs'),
]
