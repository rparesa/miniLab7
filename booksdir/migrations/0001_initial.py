# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-03 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=65)),
                ('link', models.URLField()),
                ('img', models.URLField()),
                ('author', models.ManyToManyField(to='booksdir.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ManyToManyField(to='booksdir.Publisher'),
        ),
    ]
