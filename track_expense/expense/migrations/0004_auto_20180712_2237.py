# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_expense_user_tar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='user_tar',
            field=models.ForeignKey(related_name='user_tar', to='expense.Profile', default=''),
        ),
    ]
