# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import hashlib
import time
from binascii import hexlify


def _createHash():
    hash = hashlib.sha1()
    hash.update(str(time.time()))
    return hash.hexdigest()[:-10]


class User(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=u'نام کاربر')
    last_name = models.CharField(max_length=100, verbose_name=u'نام خانوادگی')
    tel = models.CharField(max_length=14, verbose_name=u'تلفن منزل', help_text=u'به همراه کد شهر به صورت 025387654321')
    mobile = models.CharField(max_length=50, verbose_name=u'تلفن همراه')
    img = models.ImageField(default='images/gallery/portal2.jpg', upload_to='images/profile/',
                            verbose_name=u'عکس کاربر')
    score = models.IntegerField(default=0, verbose_name=u'امتیاز')
    total_spin = models.IntegerField(default=0, verbose_name=u'مجموع چرخش ها')
    username = models.CharField(max_length=30, verbose_name=u'نام کاربری', default=_createHash, unique=True)
    password = models.CharField(max_length=30, verbose_name=u'رمز عبور', default='123')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = u'کاربر'
        verbose_name_plural = u'کاربران'