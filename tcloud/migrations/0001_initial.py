# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('adv_name', models.CharField(max_length=100, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('coursename', models.CharField(max_length=100, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('mobile', models.IntegerField(serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('Advertisement', models.ForeignKey(to='tcloud.Advertisement')),
                ('course', models.ForeignKey(to='tcloud.Course')),
            ],
        ),
        migrations.CreateModel(
            name='joined',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('enquire1', models.TextField()),
                ('enquire2', models.TextField()),
                ('enquire3', models.TextField()),
                ('enquire4', models.TextField()),
                ('enquire5', models.TextField()),
                ('status', models.CharField(max_length=100, choices=[(b'f', b'followup'), (b'j', b'join'), (b'i', b'ignore')])),
                ('update', models.DateTimeField(auto_now=True)),
                ('mobile', models.ForeignKey(to='tcloud.Details')),
            ],
        ),
    ]
