from django.contrib.auth.views import PasswordResetView
from django.urls import path, include
from users.views import *

app_name = 'users'

urlpatterns = [
    path("registration/", registration, name='registration'),
    path("password_reset/",
         PasswordResetView.as_view(template_name='users/registration/password_reset_form.html'),
         name='password_reset'),
    # path("register/", Register.as_view(), name='register'),
    path("login/", login, name='login'),
    path('', include('django.contrib.auth.urls')),
]
