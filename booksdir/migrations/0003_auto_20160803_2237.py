# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-03 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksdir', '0002_auto_20160803_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(null=True),
        ),
    ]
