# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20170524_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='asdad@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
