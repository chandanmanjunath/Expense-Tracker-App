# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expense_name', models.CharField(max_length=250)),
                ('expense_description', models.CharField(max_length=4000)),
                ('price', models.FloatField(null=True, blank=True)),
                ('expense_image', models.ImageField(upload_to='users/%Y/%m/%d', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
