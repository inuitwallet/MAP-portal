# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-07 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_auto_20160507_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='on_screen_keyboard',
            field=models.BooleanField(default=False),
        ),
    ]
