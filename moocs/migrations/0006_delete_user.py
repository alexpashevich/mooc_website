# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moocs', '0005_auto_20150311_1718'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
