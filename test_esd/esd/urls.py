from django.urls import path

from esd.views import *

app_name = 'esd'

urlpatterns = [
    path('about/', about, name='about'),
    path('statisric/', statistic, name='statistic'),
    path('esdtest/', esdtest, name='esdtest'),

]
