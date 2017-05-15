# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-05-15 06:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proso_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='audit',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='audit',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='audit',
            name='info',
        ),
        migrations.RemoveField(
            model_name='audit',
            name='item_primary',
        ),
        migrations.RemoveField(
            model_name='audit',
            name='item_secondary',
        ),
        migrations.RemoveField(
            model_name='audit',
            name='user',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='audit',
        ),
        migrations.DeleteModel(
            name='Audit',
        ),
    ]
