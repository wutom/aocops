# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vminfo', '0004_auto_20170104_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host_info',
            name='vm_disk',
            field=models.IntegerField(null=True, verbose_name='\u7cfb\u7edf\u76d8'),
        ),
    ]
