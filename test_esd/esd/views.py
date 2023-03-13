from django.shortcuts import render
from random import sample
from users.models import User
from esd.models import EsdTest


def index(request):
    return render(request, 'esd/base.html')


def about(request):
    return render(request, 'esd/about.html')


def statistic(request):
    total = User.objects.all().count()
    list_pk = sample(range(total)[1:total + 1], k=10)
    users = User.objects.filter(pk__in=list_pk)
    context = {
        'users': users,
        'total': total,
    }
    return render(request, 'esd/statistic.html', context=context)


def esdtest(request):
    total = EsdTest.objects.all().count()
    list_pk = sample(range(total)[1:total + 1], k=10)
    ten_questions = EsdTest.objects.filter(pk__in=list_pk)
    context = {
        'ten_questions': ten_questions
    }
    return render(request, 'esd/esdtest.html', context=context)
