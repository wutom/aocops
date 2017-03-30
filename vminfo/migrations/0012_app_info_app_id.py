# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vminfo', '0011_auto_20170113_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='app_info',
            name='app_id',
            field=models.IntegerField(null=True, verbose_name='\u7a0b\u5e8fID'),
        ),
    ]
