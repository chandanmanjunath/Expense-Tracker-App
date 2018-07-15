# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_auto_20180712_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='user_tar',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
