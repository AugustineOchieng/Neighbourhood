# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-02 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('neighbours', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]