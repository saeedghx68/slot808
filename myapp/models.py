# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import hashlib
import time
from django.contrib.auth.models import AbstractUser


def _createHash():
    hash = hashlib.sha1()
    hash.update(str(time.time()))
    return str(hash.hexdigest()[:-30]).upper()


class User(AbstractUser):
    username = models.CharField(max_length=10, default=_createHash, verbose_name=u'نام کاربری', unique=True)
    img = models.ImageField(default='images/gallery/portal2.jpg', upload_to='images/profile/',
                            verbose_name=u'عکس کاربر')
    score = models.IntegerField(default=0, verbose_name=u'امتیاز')
    total_spin = models.IntegerField(default=0, verbose_name=u'مجموع چرخش ها')
    win = models.BooleanField(default=False, verbose_name=u'وضعیت برد')

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = u'کاربر'
        verbose_name_plural = u'کاربران'


class Awards(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'عنوان جایزه')
    description = models.TextField(verbose_name=u'توضیحات')
    img = models.ImageField(default='images/gallery/award.jpg', upload_to='images/awards/',
                            verbose_name=u'تصویر جایزه')
    min_score = models.IntegerField(verbose_name=u'حداقل امتیاز')
    max_score = models.IntegerField(verbose_name=u'حداکثر امتیاز')
    number = models.IntegerField(verbose_name=u'تعداد نفرات')
    active = models.BooleanField(default=True, verbose_name=u'وضعیت فعال بودن')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'جایزه'
        verbose_name_plural = u'جوایز'


class UserAwards(models.Model):
    user = models.ForeignKey(User, verbose_name=u'کاربر', related_name='user')
    award = models.ForeignKey(Awards, verbose_name=u'جایزه', related_name='award')

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = u'برنده'
        verbose_name_plural = u'برنده ها'