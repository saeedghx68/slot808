# -*- coding: utf-8 -*-
from random import randint
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_protect
from myapp.models import *
from django.template import Context, RequestContext
from .forms import *


@csrf_protect
def login(request):
    message1 = message2 = ''
    if request.method == 'POST':
        if request.POST.get('next', '') == 'login':
            username = request.POST.get('username', '')
            try:
                u = User.objects.get(username=username)
                if u.password == request.POST.get('password', ''):
                    request.session['user_username'] = u.username
                    request.session['total_spin'] = u.total_spin
                    return HttpResponseRedirect('/profile/')
                else:
                    message1 = u'لطفا پسورد را درست وارد کنید!'
            except User.DoesNotExist:
                message2 = u'این نام کاربری وجود ندارد!'

    if request.method == 'POST' and 'forget' in request.POST:
        pass
    return render(request, 'login.html', {'message1': message1, 'message2': message2})


def logout(request):
    try:
        del request.session['user_username']
    except KeyError:
        pass
    return HttpResponseRedirect('/login/')


@csrf_protect
def profile(request):
    c = {}
    try:
        c['firstWheel'] = 0
        c['secondWheel'] = 0
        c['thirdWheel'] = 0
        c['message'] = ''
        username = request.session['user_username']
        c['user'] = User.objects.get(username=username)
        if request.method == 'GET':
            if 'status_check' in request.GET:
                c['user'].total_spin += 1
                c['user'].save(update_fields=["total_spin"])
                c['firstWheel'] = randint(0, 9)
                c['secondWheel'] = randint(0, 9)
                c['thirdWheel'] = randint(0, 9)
                if c['firstWheel'] == c['secondWheel'] == c['thirdWheel']:
                    c['message'] = 'you win :)'
                    c['user'].score += 1
                    c['user'].save(update_fields=["score"])
                    if c['user'].score >= 10:
                        pass
                else:
                    c['message'] = 'you lose! try again...'
    except (KeyError, User.DoesNotExist):
        return HttpResponseRedirect('/login/')
    return render_to_response('profile.html', c)


@csrf_protect
def change_password(request):
    c = {}
    try:
        username = request.session['user_username']
        c['user'] = User.objects.get(username=username)

    except (KeyError, User.DoesNotExist):
        return HttpResponseRedirect('/login/')
    return render_to_response('changePass.html', c)
