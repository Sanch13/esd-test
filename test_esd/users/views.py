from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages, auth
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
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration/registration.html', context=context)


# class Register(View):
#
#     template_name = 'users/registration/registration.html'
#
#     def get(self, request):
#         context = {
#             'form': UserRegistrationForm()
#         }
#         return render(request, self.template_name, context=context)

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/registration/login.html', context=context)


# def password_reset(request):
#     if request.method == 'POST':
#         form = UserPasswordReset()
#         if form.is_valid():
