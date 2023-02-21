from django.urls import path

from esd.views import *

app_name = 'esd'

urlpatterns = [
    path('about/', about, name='about'),

]
