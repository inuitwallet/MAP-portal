# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-06 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20160406_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='client_area_animation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='disable_overlapped_content',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='focus_border_height',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='focus_border_width',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='message_duration',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mouse_click_lock',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mouse_click_lock_time',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mouse_sonar',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mouse_vanish',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='screen_reader',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='show_sounds',
            field=models.BooleanField(default=False),
        ),
    ]
