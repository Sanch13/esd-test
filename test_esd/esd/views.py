from django.shortcuts import render


def index(request):
    return render(request, 'esd/base.html')


def about(request):
    return render(request, 'esd/about.html')



