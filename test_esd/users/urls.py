from django.contrib.auth.views import LogoutView
from django.urls import path, include
from users.views import *

app_name = 'users'

urlpatterns = [
    path("registration/", registration, name='registration'),
    path("login/", login, name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
]
