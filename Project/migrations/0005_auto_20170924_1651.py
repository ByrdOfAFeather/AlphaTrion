# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 20:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0004_auto_20170924_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answerint',
            name='surveyquestions_ptr',
        ),
        migrations.RemoveField(
            model_name='answerint',
            name='user',
        ),
        migrations.RemoveField(
            model_name='answertext',
            name='surveyquestions_ptr',
        ),
        migrations.RemoveField(
            model_name='answertext',
            name='user',
        ),
        migrations.DeleteModel(
            name='AnswerInt',
        ),
        migrations.DeleteModel(
            name='AnswerText',
        ),
    ]