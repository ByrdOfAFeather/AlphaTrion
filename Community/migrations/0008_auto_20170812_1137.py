# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Community', '0007_auto_20170812_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityinst',
            name='photo',
            field=models.ImageField(default='static/Community/Community.jpg', upload_to='Community/static/Community'),
        ),
    ]
