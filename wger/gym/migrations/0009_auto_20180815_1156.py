# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-15 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0008_auto_20180803_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymconfig',
            name='weeks_inactive',
            field=models.PositiveIntegerField(default=4, help_text='Number of weeks since the last time a user logged his presence to be considered inactive', verbose_name='Reminder of inactive members'),
        ),
        migrations.AlterField(
            model_name='gymuserconfig',
            name='include_inactive',
            field=models.BooleanField(default=True, help_text='Include this user in the email list with inactive members', verbose_name='Include in inactive overview'),
        ),
    ]
