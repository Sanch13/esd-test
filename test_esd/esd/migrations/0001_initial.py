# Generated by Django 3.2.16 on 2023-03-16 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EsdTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('answer_1', models.CharField(max_length=150)),
                ('answer_2', models.CharField(max_length=150)),
                ('answer_3', models.CharField(max_length=150)),
                ('answer_4', models.CharField(max_length=150)),
                ('correct_answer', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='test_image')),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField()),
                ('date', models.DateField(auto_now_add=True, verbose_name='Время создания')),
            ],
        ),
    ]
