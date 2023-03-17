from django.db import models
from users.models import User


class EsdTest(models.Model):
    question = models.CharField(max_length=250)
    answer_1 = models.CharField(max_length=150)
    answer_2 = models.CharField(max_length=150)
    answer_3 = models.CharField(max_length=150)
    answer_4 = models.CharField(max_length=150)
    correct_answer = models.CharField(max_length=150)
    image = models.ImageField(upload_to='test_image',
                              blank=True)

    class Meta:
        verbose_name = 'ESD тестирование'
        verbose_name_plural = 'ESD тестирование'
        ordering = ['id']


class Statistic(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name="Время создания")

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'
        ordering = ['id']
