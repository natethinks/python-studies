# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 04:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160922_0447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_test',
            new_name='question_text',
        ),
    ]
