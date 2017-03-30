# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vminfo', '0008_auto_20170110_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app_info',
            name='app_alarm',
        ),
        migrations.AddField(
            model_name='app_info',
            name='app_alarm',
            field=models.CharField(max_length=12, null=True, verbose_name='\u62a5\u8b66\u7c7b\u578b', blank=True),
        ),
        migrations.AlterField(
            model_name='app_info',
            name='app_label',
            field=models.CharField(max_length=12, null=True, verbose_name='\u4e1a\u52a1\u6807\u7b7e', blank=True),
        ),
        migrations.RemoveField(
            model_name='app_info',
            name='app_manager',
        ),
        migrations.AddField(
            model_name='app_info',
            name='app_manager',
            field=models.CharField(max_length=12, null=True, verbose_name='\u7ef4\u62a4\u8005', blank=True),
        ),
        migrations.AlterField(
            model_name='app_info',
            name='app_vm_id',
            field=models.IntegerField(null=True, verbose_name='\u4e3b\u673aID'),
        ),
    ]
