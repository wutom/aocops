# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20161212_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='aocops_indexBulletin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Bull_remark', models.TextField(max_length=256, null=True, verbose_name='\u6587\u6863\u5907\u6ce8', blank=True)),
            ],
            options={
                'db_table': 'index_aocops_indexBulletin',
                'verbose_name': '\u516c\u53f8\u516c\u544a',
                'verbose_name_plural': '\u516c\u53f8\u516c\u544a',
            },
        ),
    ]
