# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moocs', '0010_auto_20150406_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mooc',
            old_name='description',
            new_name='description_short',
        ),
        migrations.AddField(
            model_name='mooc',
            name='curriculum',
            field=models.TextField(default='cur'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mooc',
            name='description_full',
            field=models.TextField(default='descr'),
            preserve_default=False,
        ),
    ]
