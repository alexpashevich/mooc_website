# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moocs', '0008_auto_20150406_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='mooc',
            name='subtitles',
            field=models.ManyToManyField(related_name='mooc_subtitles_language', to='moocs.Language', null=True),
            preserve_default=True,
        ),
    ]
