# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('place_name', models.TextField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('info', models.TextField()),
                ('place_id', models.TextField()),
                ('group_name', models.CharField(max_length=200)),
                ('capital', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
