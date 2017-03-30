# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vminfo', '0006_host_info_vm_manage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vm_info',
            name='vm_label',
        ),
        migrations.RemoveField(
            model_name='vm_info',
            name='vm_location',
        ),
        migrations.RemoveField(
            model_name='vm_info',
            name='vm_manager',
        ),
        migrations.RemoveField(
            model_name='vm_info',
            name='vm_status',
        ),
        migrations.AlterModelOptions(
            name='host_info',
            options={'verbose_name': '\u4e3b\u673a\u4fe1\u606f', 'verbose_name_plural': '\u4e3b\u673a\u4fe1\u606f'},
        ),
        migrations.DeleteModel(
            name='vm_info',
        ),
    ]
