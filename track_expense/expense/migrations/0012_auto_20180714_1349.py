# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0011_auto_20180714_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='expense_image',
            field=models.ImageField(upload_to='images/%Y/%m/%d', blank=True),
        ),
    ]
