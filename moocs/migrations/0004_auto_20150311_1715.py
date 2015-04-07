# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moocs', '0003_auto_20150311_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='text',
            new_name='description',
        ),
        migrations.AddField(
            model_name='lesson',
            name='title',
            field=models.TextField(default='x'),
            preserve_default=False,
        ),
    ]
