# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_name_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flavour',
            name='flavour_image',
            field=models.FileField(upload_to=''),
        ),
    ]
