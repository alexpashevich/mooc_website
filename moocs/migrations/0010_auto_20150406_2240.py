# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moocs', '0009_mooc_subtitles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mooc',
            old_name='beging_date',
            new_name='begin_date',
        ),
        migrations.RemoveField(
            model_name='lector',
            name='mooc',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='mooc',
        ),
        migrations.AddField(
            model_name='mooc',
            name='lector',
            field=models.ForeignKey(to='moocs.Lector', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mooc',
            name='subtitles',
            field=models.ManyToManyField(related_name='mooc_subtitles_language', to='moocs.Language'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mooc',
            name='university',
            field=models.ForeignKey(to='moocs.University'),
            preserve_default=True,
        ),
    ]
