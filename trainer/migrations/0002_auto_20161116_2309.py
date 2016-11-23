# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32)),
                ('slug', models.SlugField(max_length=128)),
                ('mode', models.IntegerField(choices=[(0, 'must'), (1, 'may'), (2, 'mustnot')])),
                ('description', models.CharField(max_length=2048)),
                ('rule', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='sentence',
            name='comma_list',
            field=models.CommaSeparatedIntegerField(default='0', max_length=255),
        ),
        migrations.AddField(
            model_name='sentence',
            name='comma_select',
            field=models.CommaSeparatedIntegerField(default='0', max_length=255),
        ),
        migrations.AddField(
            model_name='sentence',
            name='total_submits',
            field=models.IntegerField(default='0', max_length=25),
        ),
    ]
