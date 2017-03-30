# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmset', '0001_initial'),
        ('vminfo', '0014_auto_20170116_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='host_info',
            name='vm_status',
            field=models.ForeignKey(verbose_name='\u4e3b\u673a\u7c7b\u578b', blank=True, to='vmset.info_status', null=True),
        ),
    ]
