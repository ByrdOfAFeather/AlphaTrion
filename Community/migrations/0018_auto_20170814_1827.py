# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Community', '0017_communitygameratings_like_to_see_again'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityinst',
            name='minutes_ended_early',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.AddField(
            model_name='game',
            name='number_of_participants',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='communitygameratings',
            name='like_to_see_again',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No')], default='n', max_length=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(blank=True, default='No decription'),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
