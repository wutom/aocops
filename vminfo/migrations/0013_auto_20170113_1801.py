# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vminfo', '0012_app_info_app_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_info',
            name='app_id',
            field=models.CharField(max_length=20, null=True, verbose_name='\u7a0b\u5e8fID'),
        ),
    ]
