# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0012_auto_20180714_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='expense_description',
            field=models.TextField(max_length=2048),
        ),
    ]
