# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vminfo', '0005_auto_20170105_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='host_info',
            name='vm_manage',
            field=models.CharField(max_length=12, null=True, verbose_name='\u7ef4\u62a4\u8005'),
        ),
    ]
