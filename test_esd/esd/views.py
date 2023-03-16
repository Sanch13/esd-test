from django.http import HttpResponseRedirect
from service.middleware import *
from django.shortcuts import render
from esd.models import *
from django.urls import reverse


def index(request):
    return render(request, 'esd/base.html')


def about(request):
    return render(request, 'esd/about.html')


def statistic(request):
    # total = User.objects.all().count()
    # list_pk = list(range(1, total + 1))
    # users = User.objects.filter(pk__in=list_pk)
    total = User.objects.all().count()
    users = User.objects.all()
    context = {
        'users': users,
        'total': total,
    }
    return render(request, 'esd/statistic.html', context=context)


def esdtest(request):
    return render(request, 'esd/esdtest.html')


def question(request):
    list_question = user_data.get('questions')
    print('Осталось вопросов: ', len(list_question))
    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        question_id = request.POST.get('question_id')
        question = EsdTest.objects.get(pk=question_id)
        if question.correct_answer == user_answer:
            user_data['score'] += 1
            print('Количество правильных ответов: ', user_data.get('score'))
        if len(list_question) == 0:
            user = User.objects.get(username=request.user.username)
            Statistic(score=user_data.get('score'), user_id=user.pk).save()
            user_data['score'] = 0
            user_data['questions'] = get_random_questions()
            return HttpResponseRedirect(reverse('esd:score'))

    question = list_question.pop()
    context = {
        'question': question,
    }
    return render(request, 'esd/esdquestion.html', context=context)


def score(request):
    result = Statistic.objects.filter(pk=request.user.pk)
    context = {
        'result': result
    }
    return render(request, 'esd/score.html', context=context)
