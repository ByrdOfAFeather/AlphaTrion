# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Senate', '0008_auto_20171105_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minutes',
            name='embed_link',
            field=models.TextField(default='Embed Code Goes Here!', help_text='To get a embed link goto file -> publish to web -> embed -> copy the link into here'),
        ),
    ]
