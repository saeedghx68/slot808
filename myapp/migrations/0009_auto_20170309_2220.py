# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-09 18:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_category_gallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': '\u062f\u0633\u062a\u0647 \u0628\u0646\u062f\u06cc \u0645\u062d\u0635\u0648\u0644\u0627\u062a', 'verbose_name_plural': '\u062f\u0633\u062a\u0647 \u0628\u0646\u062f\u06cc \u0645\u062d\u0635\u0648\u0644\u0627\u062a'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ['upload_date'], 'verbose_name': '\u06af\u0627\u0644\u0631\u06cc \u0645\u062d\u0635\u0648\u0644\u0627\u062a', 'verbose_name_plural': '\u06af\u0627\u0644\u0631\u06cc \u0645\u062d\u0635\u0648\u0644\u0627\u062a'},
        ),
    ]