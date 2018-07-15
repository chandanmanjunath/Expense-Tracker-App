# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0009_auto_20180712_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='expense_image',
            field=models.ImageField(upload_to='images/%Y/%m/%d', blank=True),
        ),
    ]
