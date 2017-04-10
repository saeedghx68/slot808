# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-12 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20170312_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awards',
            name='img',
            field=models.ImageField(default='images/gallery/award.jpg', help_text='\u0627\u0646\u062f\u0627\u0632\u0647 \u062a\u0635\u0648\u06cc\u0631: 370 * 620 \u067e\u06cc\u06a9\u0633\u0644', upload_to='images/awards/', verbose_name='\u062a\u0635\u0648\u06cc\u0631 \u062c\u0627\u06cc\u0632\u0647'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='small_img',
            field=models.ImageField(default='images/gallery/defaults.jpg', help_text='\u0627\u0646\u062f\u0627\u0632\u0647 \u062a\u0635\u0648\u06cc\u0631: 300 * 212 \u067e\u06cc\u06a9\u0633\u0644', upload_to='images/gallery/', verbose_name='\u062a\u0635\u0648\u06cc\u0631 \u06a9\u0648\u0686\u06a9'),
        ),
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(default='images/gallery/portal2.jpg', help_text='\u0627\u0646\u062f\u0627\u0632\u0647 \u062a\u0635\u0648\u06cc\u0631: 128 * 128 \u067e\u06cc\u06a9\u0633\u0644', upload_to='images/profile/', verbose_name='\u0639\u06a9\u0633 \u06a9\u0627\u0631\u0628\u0631'),
        ),
    ]