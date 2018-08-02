# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-21 18:00
from __future__ import unicode_literals

from django.db import migrations, models


def copy_name(apps, schema_editor):
    '''
    Copies the exercise name to the original name field
    '''
    Excercise = apps.get_model("exercises", "Exercise")
    for exercise in Excercise.objects.all():
        exercise.name_original = exercise.name
        exercise.save()


def capitalize_name(apps, schema_editor):
    '''
    Capitalizes the name of the exercises

    The algorithm is copied here as it was implemented on the day the migration
    was written.
    '''
    def capitalize(input):
        out = []
        for word in input.split(' '):
            if len(word) > 2 and word[0] != u'ß':
                out.append(word[:1].upper() + word[1:])
            else:
                out.append(word)
        return ' '.join(out)

    Excercise = apps.get_model("exercises", "Exercise")
    for exercise in Excercise.objects.all():
        exercise.name = capitalize(exercise.name_original)
        exercise.save()


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_auto_20150307_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='name_original',
            field=models.CharField(default='', max_length=200,
                                   verbose_name='Name'),
        ),
        migrations.RunPython(copy_name,
                             reverse_code=migrations.RunPython.noop),
        migrations.RunPython(capitalize_name,
                             reverse_code=migrations.RunPython.noop),
    ]
