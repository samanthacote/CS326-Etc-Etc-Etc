# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rendezvous', '0002_auto_20171031_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='events',
            field=models.ManyToManyField(blank=True, to='rendezvous.Event'),
        ),
    ]