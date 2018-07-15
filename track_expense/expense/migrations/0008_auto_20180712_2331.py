# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0007_auto_20180712_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='user_tar',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
