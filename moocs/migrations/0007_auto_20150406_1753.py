# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('moocs', '0006_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('language_name', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('abbreviation', models.TextField()),
                ('full_name', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='mooc',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='mooc',
            name='beging_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 14, 53, 7, 186623, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mooc',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 14, 53, 12, 578577, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mooc',
            name='language',
            field=models.ForeignKey(related_name='mooc_language', null=True, to='moocs.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mooc',
            name='subtitles',
            field=models.ForeignKey(related_name='mooc_subtitles_language', null=True, to='moocs.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mooc',
            name='workload',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
