# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moocs', '0004_auto_20150311_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='number',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='module',
            name='number',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
