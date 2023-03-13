from django.contrib import admin
from esd.models import *


@admin.register(EsdTest)
class EsdTestAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_1', 'answer_2', 'answer_3', 'answer_4', 'correct_answer')
