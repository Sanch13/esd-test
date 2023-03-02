from django.shortcuts import render

from users.models import User


def index(request):
    return render(request, 'esd/base.html')


def about(request):
    return render(request, 'esd/about.html')


def statistic(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'esd/statistic.html', context=context)


def esdtest(request):
    return render(request, 'esd/esdtest.html')
