from django.http import HttpResponseRedirect
from service.middleware import *
from django.shortcuts import render
from esd.models import *
from django.urls import reverse
from django.db.models import Max, Subquery, OuterRef


def index(request):
    return render(request, 'esd/base.html')


def about(request):
    return render(request, 'esd/about.html')


def statistic(request):
    # Display latest statistics
    total = User.objects.count()
    latest_results = Statistic.objects.filter(
        time_create__in=Subquery(
            Statistic.objects.filter(user_id=OuterRef('user_id'))
            .values('user_id')
            .annotate(latest_time=Max('time_create'))
            .values('latest_time')
        )
    ).select_related('user')
    context = {
        'total': total,
        'latest_results': latest_results,
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
    result = Statistic.objects.filter(user_id=request.user.pk).order_by('-time_create').first()
    # Display the latest user data with the test passed
    context = {
        'result': result
    }
    return render(request, 'esd/score.html', context=context)
