# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense', '0002_expense'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='user_tar',
            field=models.ForeignKey(related_name='user_tar', default='', to=settings.AUTH_USER_MODEL),
        ),
    ]
