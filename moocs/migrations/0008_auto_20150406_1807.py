# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moocs', '0007_auto_20150406_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mooc',
            name='subtitles',
        ),
        migrations.AddField(
            model_name='mooc',
            name='university',
            field=models.ForeignKey(to='moocs.University', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mooc',
            name='language',
            field=models.ForeignKey(related_name='mooc_language', to='moocs.Language'),
            preserve_default=True,
        ),
    ]
