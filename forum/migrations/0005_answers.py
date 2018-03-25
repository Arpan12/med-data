# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-01 09:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0004_auto_20170527_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=2000)),
                ('upvotes', models.IntegerField(default=0)),
                ('comments', models.CharField(max_length=250)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
