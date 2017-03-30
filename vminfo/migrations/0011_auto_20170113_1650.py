# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vminfo', '0010_auto_20170113_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app_info',
            old_name='app_ipadd_port',
            new_name='app_listen',
        ),
        migrations.RenameField(
            model_name='app_info',
            old_name='app_path',
            new_name='app_name',
        ),
        migrations.RenameField(
            model_name='app_info',
            old_name='app_vm_hostname',
            new_name='hostname',
        ),
        migrations.RemoveField(
            model_name='app_info',
            name='app_log_path',
        ),
        migrations.AddField(
            model_name='app_info',
            name='app_pid',
            field=models.IntegerField(null=True, verbose_name='\u7a0b\u5e8fPID'),
        ),
    ]
