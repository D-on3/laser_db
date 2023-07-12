from django.urls import path
from . import views

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Login and Logout URLs
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Registration URL
    path('register/', views.registration, name='register'),

    # User Profile URL
    path('profile/', views.profile, name='profile'),

    # Author URLs
    path('authors/', views.author_list, name='author_list'),
    path('authors/create/', views.author_create, name='author_create'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('authors/<int:author_id>/update/', views.author_update, name='author_update'),

    # Machine URLs
    path('machines/', views.machine_list, name='machine_list'),
    path('machines/create/', views.machine_create, name='machine_create'),
    path('machines/<int:machine_id>/', views.machine_detail, name='machine_detail'),
    path('machines/<int:machine_id>/update/', views.machine_update, name='machine_update'),

    # Result URLs
    path('results/', views.result_list, name='result_list'),
    path('results/create/', views.result_create, name='result_create'),
    path('results/<int:result_id>/', views.result_detail, name='result_detail'),
    path('results/<int:result_id>/update/', views.result_update, name='result_update'),
]
