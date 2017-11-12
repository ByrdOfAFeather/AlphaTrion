# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0004_auto_20171111_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade_level',
            field=models.PositiveIntegerField(choices=[(9, 9), (10, 10), (11, 11), (12, 12)], default=3),
        ),
    ]
