from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path("registration/", registration, name='registration'),
    # path("register/", Register.as_view(), name='register'),
    path("login/", login, name='login'),
]
