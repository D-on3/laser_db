from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('login/email/', views.login_email_view, name='login-email'),
    path('login/email_or_username/', views.login_email_or_username_view, name='login-email-or-username'),
    path('register/', views.registration_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/activate/<str:activation_key>/', views.activate_profile, name='activate-profile'),
    path('profile/reset_password/', views.reset_password_request, name='reset-password-request'),
    path('profile/reset_password/<str:reset_key>/', views.reset_password_confirm, name='reset-password-confirm'),
    path('profile/resend_activation/', views.resend_activation_view, name='resend-activation'),
    path('profile/change_password/', views.change_password_view, name='change-password'),
    path('profile/change_email/', views.change_email_view, name='change-email'),
    path('profile/change_profile/', views.change_profile_view, name='change-profile'),
]
