# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-21 07:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20180821_1041'),
        ('exercises', '0006_auto_20180815_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='license_author_link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.LicenseAuthor', verbose_name='LicenseAuthor'),
        ),
        migrations.AddField(
            model_name='exerciseimage',
            name='license_author_link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.LicenseAuthor', verbose_name='LicenseAuthor'),
        ),
    ]
