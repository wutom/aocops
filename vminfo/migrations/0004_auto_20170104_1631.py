# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vminfo', '0003_auto_20170104_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host_info',
            name='vm_label',
        ),
        migrations.RemoveField(
            model_name='host_info',
            name='vm_manager',
        ),
        migrations.RemoveField(
            model_name='host_info',
            name='vm_status',
        ),
    ]
