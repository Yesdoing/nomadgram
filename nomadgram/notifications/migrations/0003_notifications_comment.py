# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-05 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20180305_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
