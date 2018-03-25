# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-14 09:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0005_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='comments',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.RemoveField(
            model_name='answers',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='answers',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='Answer_upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]