# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aocops_indextype',
            name='it_remark',
            field=models.TextField(max_length=256, null=True, verbose_name='\u5206\u7c7b\u5907\u6ce8', blank=True),
        ),
    ]
