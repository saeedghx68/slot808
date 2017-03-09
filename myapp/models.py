# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import hashlib
import time
from django.contrib.auth.models import AbstractUser
from datetime import datetime


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


class Lottery(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'عنوان قرعه کشی')
    description = models.TextField(default="", verbose_name=u'توضیحات')
    active = models.BooleanField(default=True, verbose_name=u'وضعیت فعال بودن')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'قرعه کشی'
        verbose_name_plural = u'قرعه کشی ها'


class Awards(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'عنوان جایزه')
    description = models.TextField(default="", verbose_name=u'توضیحات')
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
        return self.user.username

    class Meta:
        verbose_name = u'برنده'
        verbose_name_plural = u'برنده ها'

#****************Declare gallery model

class Category(models.Model):
    name = models.CharField(default='other',max_length=50,verbose_name=u'نام دسته')
    upload_date = models.DateTimeField(default=datetime.now, blank=True)

    def as_json(self):
        return {
                'id': self.id - 1,
                'name': self.name,
                }

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['upload_date']
        verbose_name = u'دسته بندی محصولات'
        verbose_name_plural = u'دسته بندی محصولات'

class Gallery(models.Model):
    cat_id = models.ForeignKey(Category,verbose_name=u'گروه')
    small_img = models.ImageField(default='images/gallery/defaults.jpg',upload_to='images/gallery/',verbose_name=u'تصویر کوچک')
    large_img = models.ImageField(default='images/gallery/defaults.jpg',upload_to='images/gallery/',verbose_name=u'تصویر بزرگ')
    alt = models.CharField(default='',max_length=100,verbose_name=u'عنوان')
    upload_date = models.DateTimeField(default=datetime.now, blank=True)

    def as_json(self):
        return {
                'id':self.id - 1,
                'imgs': str(self.small_img),
                'imgl': str(self.large_img),
                'alt':self.alt,
                }

    def __unicode__(self):
        return self.alt

    class Meta:
        ordering = ['upload_date']
        verbose_name = u'گالری محصولات'
        verbose_name_plural = u'گالری محصولات'
#*****************End of gallery model
