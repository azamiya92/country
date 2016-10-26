# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('capital', models.CharField(max_length=255, null=True, blank=True)),
                ('population', models.IntegerField(null=True, blank=True)),
                ('flag', models.ImageField(null=True, upload_to=b'flags', blank=True)),
            ],
        ),
    ]
