# -*- coding: utf-8 -*-
from random import randint
from django.http import HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_protect
from myapp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model, authenticate
from django.template import Context, RequestContext
from .forms import *
import csv
from django.http import StreamingHttpResponse
import cStringIO as StringIO


User = get_user_model()

@csrf_protect
def user_login(request):

    if request.method == 'POST':
        data = request.POST
        username = data.get('username', '')
        password = data.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/profile/')
    else:
        return render(request, 'login.html')


def user_logout(request):
    try:
        logout(request)
    except KeyError:
        pass
    return HttpResponseRedirect('/login/')


@csrf_protect
def get_lattery(request):
    c = {}
    user = request.user
    c['message'] = ''
    c['firstWheel'] = randint(0, 9)
    c['secondWheel'] = randint(0, 9)
    c['thirdWheel'] = randint(0, 9)
    user.total_spin += 1
    user.save(update_fields=["total_spin"])
    c['totalSpin'] = user.total_spin
    if c['firstWheel'] == c['secondWheel'] == c['thirdWheel']:
        c['message'] = 'you win :)'
        user.score += 1
        user.save(update_fields=["score"])
        c['score'] = user.score
        if user.score >= 10:
            pass
    else:
        c['message'] = 'you lose! try again...'
    return JsonResponse(c)


@csrf_protect
def profile(request):
    c = {}
    try:
        c['message'] = ''
        c['user'] = request.user
        print c['user']
    except Exception as ex:
        return HttpResponseRedirect('/login/')
    return render_to_response('profile.html', c)


@csrf_protect
def change_password(request):
    c = {}
    try:
        if request.method == 'POST':
            data = request.POST

    except (KeyError, User.DoesNotExist):
        return HttpResponseRedirect('/login/')
    return render_to_response('changePass.html', c)
