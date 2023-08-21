from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
