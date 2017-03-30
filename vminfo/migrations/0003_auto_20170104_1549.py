# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vminfo', '0002_auto_20170104_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host_info',
            name='machine_id',
            field=models.IntegerField(null=True, verbose_name='\u4e3b\u673aID'),
        ),
        migrations.AlterField(
            model_name='host_info',
            name='vm_cpu',
            field=models.IntegerField(null=True, verbose_name='CPU'),
        ),
        migrations.AlterField(
            model_name='host_info',
            name='vm_mem',
            field=models.IntegerField(null=True, verbose_name='\u5185\u5b58'),
        ),
    ]
