from django.urls import path
from accounts.views import *
from django.contrib.auth import views as auth_views


# We are adding a URL called /home
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="/accounts/login")),
    path('register/',register, name="register"),
    path('password/', change_password, name='change_password'),
]
