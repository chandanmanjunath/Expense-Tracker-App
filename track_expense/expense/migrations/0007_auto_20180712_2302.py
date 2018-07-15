# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0006_auto_20180712_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='user_tar',
            field=models.CharField(max_length=250),
        ),
    ]
