# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moocs', '0002_auto_20150311_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('number', models.IntegerField(unique=True)),
                ('text', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('lesson', models.ForeignKey(to='moocs.Lesson')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='user',
            name='exercise',
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
    ]
