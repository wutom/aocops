# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmset', '0001_initial'),
        ('vminfo', '0013_auto_20170113_1801'),
    ]

    operations = [
        migrations.DeleteModel(
            name='app_info_alarm',
        ),
        migrations.DeleteModel(
            name='info_location',
        ),
        migrations.RemoveField(
            model_name='info_manager',
            name='mana_group',
        ),
        migrations.RemoveField(
            model_name='info_manager',
            name='mana_label',
        ),
        migrations.DeleteModel(
            name='info_status',
        ),
        migrations.RemoveField(
            model_name='app_info',
            name='app_alarm',
        ),
        migrations.AddField(
            model_name='app_info',
            name='app_alarm',
            field=models.ManyToManyField(to='vmset.app_info_alarm', null=True, verbose_name='\u62a5\u8b66\u7c7b\u578b', blank=True),
        ),
        migrations.AlterField(
            model_name='app_info',
            name='app_label',
            field=models.ForeignKey(verbose_name='\u4e1a\u52a1\u6807\u7b7e', blank=True, to='vmset.info_label', null=True),
        ),
        migrations.RemoveField(
            model_name='app_info',
            name='app_manager',
        ),
        migrations.AddField(
            model_name='app_info',
            name='app_manager',
            field=models.ManyToManyField(to='vmset.info_manager', null=True, verbose_name='\u7ef4\u62a4\u8005', blank=True),
        ),
        migrations.AlterField(
            model_name='host_info',
            name='vm_location',
            field=models.ForeignKey(verbose_name='\u653e\u7f6e\u4f4d\u7f6e', blank=True, to='vmset.info_location', null=True),
        ),
        migrations.RemoveField(
            model_name='host_info',
            name='vm_manage',
        ),
        migrations.AddField(
            model_name='host_info',
            name='vm_manage',
            field=models.ManyToManyField(to='vmset.info_manager', null=True, verbose_name='\u7ef4\u62a4\u8005', blank=True),
        ),
        migrations.DeleteModel(
            name='info_group',
        ),
        migrations.DeleteModel(
            name='info_label',
        ),
        migrations.DeleteModel(
            name='info_manager',
        ),
    ]
