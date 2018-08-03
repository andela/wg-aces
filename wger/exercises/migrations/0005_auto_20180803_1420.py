# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-03 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0004_auto_20180801_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='license_author',
            field=models.CharField(
                blank=True,
                help_text='If you are not the author, enter the name or source\
                here. This is needed for some licenses e.g. the CC-BY-SA.',
                max_length=50, null=True, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='exerciseimage',
            name='is_main',
            field=models.BooleanField(
                default=False,
                help_text='Tick the box if you want to set this image\
                as the main one for the exercise (will be shown e.g. in\
                the search). The first image is automatically marked by\
                the system.',
                verbose_name='Main picture'),
        ),
        migrations.AlterField(
            model_name='exerciseimage',
            name='license_author',
            field=models.CharField(
                blank=True,
                help_text='If you are not the author, enter the name or\
                source here. This is needed for some licenses e.g. the\
                CC-BY-SA.',
                max_length=50, null=True, verbose_name='Author'),
        ),
    ]
