from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True)
    tab_number = models.PositiveIntegerField(blank=True, null=True)
