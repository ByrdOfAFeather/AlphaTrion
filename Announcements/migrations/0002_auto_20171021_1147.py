# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 15:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Announcements', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['occuring_date']},
        ),
    ]
