# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('text', models.TextField()),
                ('status', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lector',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.TextField()),
                ('info', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mooc',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.TextField()),
                ('login', models.TextField()),
                ('password', models.TextField()),
                ('exercise', models.ForeignKey(to='moocs.Exercise')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='lesson',
            name='mooc',
            field=models.ForeignKey(to='moocs.Mooc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lector',
            name='mooc',
            field=models.ForeignKey(to='moocs.Mooc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exercise',
            name='lesson',
            field=models.ForeignKey(to='moocs.Lesson'),
            preserve_default=True,
        ),
    ]
