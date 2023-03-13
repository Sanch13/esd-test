from django.db import models


class EsdTest(models.Model):
    question = models.CharField(max_length=250)
    answer_1 = models.CharField(max_length=150)
    answer_2 = models.CharField(max_length=150)
    answer_3 = models.CharField(max_length=150)
    answer_4 = models.CharField(max_length=150)
    correct_answer = models.CharField(max_length=150)
    image = models.ImageField(upload_to='test_image', blank=True)
