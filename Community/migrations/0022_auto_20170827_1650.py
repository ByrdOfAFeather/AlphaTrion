# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 20:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Community', '0021_auto_20170817_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitygameratings',
            name='game_rating',
            field=models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=5),
        ),
        migrations.AlterField(
            model_name='communityinst',
            name='date',
            field=models.DateField(default=datetime.date(2017, 8, 27)),
        ),
    ]
