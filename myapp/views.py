# -*- coding: utf-8 -*-
from random import randint
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound, JsonResponse, HttpResponse
from django.shortcuts import render_to_response, render, redirect
from django.views.decorators.csrf import csrf_protect
from myapp.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.template import Context, RequestContext
from .forms import *
import csv
from django.http import StreamingHttpResponse
import cStringIO as StringIO

User = get_user_model()

def home(request):
    return render_to_response('index.html')

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
                return HttpResponse("!اکانت شما غیر  فعال است")
        else:
            message = "لطفا نام کاربری و رمز عبور را درست وارد نمایید."
            return render(request, 'login.html', {'message': message})
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
    award = None
    c['btn_status'] = ''
    c['message'] = ''

    try:
        if user.win:
            c['btn_status'] = 'disabled'
            c['message'] = u'شما قبلا در قرعه کشی شرکت کرده اید.'
        else:
            awards = Awards.objects.filter(active=True)
            if len(awards) == 0:
                c['btn_status'] = 'disabled'
                c['message'] = u'قرعه کشی به پایان رسیده است!'
            else:
                for award_obj in awards:
                    if award_obj.min_score < user.score < award_obj.max_score:
                        award = award_obj
                if award is None:
                    c['btn_status'] = 'disabled'
                    c['message'] = u'شما امتیاز لازم برای شرکت در قرعه کشی را ندارید!'
                else:
                    c['secondWheel'] = randint(0, 9)
                    c['firstWheel'] = randint(0, 9)
                    c['thirdWheel'] = randint(0, 9)
                    if c['firstWheel'] == c['secondWheel'] == c['thirdWheel']:
                        UserAwards(user=user, award=award).save()
                        award.number -= 1
                        award.save(update_fields=["number"])
                        if award.number <= 0:
                            award.active = False
                            award.save(update_fields=["active"])
                        user.win = True
                        user.save()
                        c['message'] = ' تبریک! شما برنده شدید :)'
                    else:
                        c['message'] = 'شما برنده نشدید! مجددا تلاش کنید...'
    except Exception as ex:
        print ex
    return JsonResponse(c)


@login_required(login_url="/login/")
def profile(request):
    c = {}
    c['btn_status'] = ''
    award = None

    try:
        c['lottery'] = Lottery.objects.filter(active=True)[0]
        c['active_awards'] = Awards.objects.filter(active=True)
        c['user'] = request.user
        if c['user'].win:
            c['btn_status'] = 'disabled'
            c['message'] = u'شما قبلا در قرعه کشی شرکت کرده اید.'
        else:
            active_awards = c['active_awards']
            if len(active_awards) == 0:
                c['btn_status'] = 'disabled'
                c['message'] = u'قرعه کشی به پایان رسیده است.'
            else:
                for award_obj in active_awards:
                    if award_obj.min_score < c['user'].score < award_obj.max_score:
                        award = award_obj
                if award is None:
                    c['btn_status'] = 'disabled'
                    c['message'] = u'شما امتیاز لازم برای شرکت در قرعه کشی را ندارید.'

    except Exception as ex:
        return HttpResponseRedirect('/login/')
    return render_to_response('profile.html', c)


@login_required(login_url="/login/")
def change_password(request):
    c = {}
    c['user'] = request.user

    if request.method == 'POST':
        c['form'] = PasswordChangeForm(request.user, request.POST)
        if c['form'].is_valid():
            user = c['form'].save()
            update_session_auth_hash(request, user)
            c['message'] = u'رمز عبور شما با موفقیت به روز رسانی شد.'
    else:
        c['form'] = PasswordChangeForm(request.user)
    return render(request, 'changePass.html', c)
