# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vminfo', '0009_auto_20170110_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_info',
            name='app_ipadd_port',
            field=models.CharField(max_length=16, null=True, verbose_name=b'\xe7\xa8\x8b\xe5\xba\x8f\xe7\x9b\x91\xe5\x90\xac'),
        ),
        migrations.AlterField(
            model_name='app_info',
            name='app_log_path',
            field=models.IntegerField(null=True, verbose_name='\u7a0b\u5e8fID'),
        ),
        migrations.AlterField(
            model_name='app_info',
            name='app_path',
            field=models.CharField(max_length=20, null=True, verbose_name='\u7a0b\u5e8f\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='app_info',
            name='app_vm_hostname',
            field=models.CharField(max_length=24, null=True, verbose_name='\u4e3b\u673a\u540d\u79f0'),
        ),
    ]
