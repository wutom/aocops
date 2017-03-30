# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vminfo', '0007_auto_20170110_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host_info',
            name='vm_location',
            field=models.CharField(max_length=12, null=True, verbose_name='\u653e\u7f6e\u4f4d\u7f6e', blank=True),
        ),
        migrations.AlterField(
            model_name='host_info',
            name='vm_manage',
            field=models.CharField(max_length=12, null=True, verbose_name='\u7ef4\u62a4\u8005', blank=True),
        ),
        migrations.AlterField(
            model_name='host_info',
            name='vm_remark',
            field=models.TextField(max_length=256, null=True, verbose_name='\u5907\u6ce8\u4fe1\u606f', blank=True),
        ),
    ]
