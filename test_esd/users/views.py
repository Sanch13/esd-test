from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.views import View

from users.forms import *


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Вы успешно зарегистрировались! '
                             'Войдите под своим логином и паролем в систему')
            return HttpResponseRedirect(reverse('login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'registration/registration.html', context=context)


# class Register(View):
#
#     template_name = 'registration/registration.html'
#
#     def get(self, request):
#         context = {
#             'form': UserRegistrationForm()
#         }
#         return render(request, self.template_name, context=context)

def login(request):
    form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/registration/login.html', context=context)
