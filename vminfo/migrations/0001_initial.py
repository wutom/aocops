# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='app_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_path', models.CharField(max_length=50, null=True, verbose_name='\u7a0b\u5e8f\u8def\u5f84')),
                ('app_vm_hostname', models.CharField(max_length=32, null=True, verbose_name='\u4e3b\u673a\u540d\u79f0')),
                ('app_ipadd_port', models.CharField(max_length=20, null=True, verbose_name=b'\xe7\xa8\x8b\xe5\xba\x8f\xe7\x9b\x91\xe5\x90\xac')),
                ('app_log_path', models.CharField(max_length=50, null=True, verbose_name='\u65e5\u5fd7\u8def\u5f84')),
                ('app_vm_id', models.CharField(max_length=32, null=True, verbose_name='\u4e3b\u673aID')),
                ('app_remark', models.TextField(max_length=256, null=True, verbose_name='\u5907\u6ce8\u4fe1\u606f')),
            ],
            options={
                'verbose_name': '\u7a0b\u5e8f\u4fe1\u606f',
                'verbose_name_plural': '\u7a0b\u5e8f\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='app_info_alarm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alarm_types', models.CharField(max_length=10, null=True, verbose_name='\u62a5\u8b66\u7c7b\u578b')),
            ],
            options={
                'verbose_name': '\u62a5\u8b66\u7c7b\u578b',
                'verbose_name_plural': '\u62a5\u8b66\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='info_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=16, null=True, verbose_name='\u4e1a\u52a1\u7ec4\u540d')),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u7ec4\u540d',
                'verbose_name_plural': '\u4e1a\u52a1\u7ec4\u540d',
            },
        ),
        migrations.CreateModel(
            name='info_label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=16, verbose_name='\u4e1a\u52a1\u6807\u7b7e')),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u6807\u7b7e',
                'verbose_name_plural': '\u4e1a\u52a1\u6807\u7b7e',
            },
        ),
        migrations.CreateModel(
            name='info_location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=20, verbose_name='\u653e\u7f6e\u4f4d\u7f6e')),
            ],
            options={
                'verbose_name': '\u653e\u7f6e\u4f4d\u7f6e',
                'verbose_name_plural': '\u653e\u7f6e\u4f4d\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='info_manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mana_name', models.CharField(max_length=12, null=True, verbose_name='\u7ef4\u62a4\u8005\u59d3\u540d')),
                ('mana_phone', models.CharField(max_length=12, null=True, verbose_name='\u7ef4\u62a4\u8005\u7535\u8bdd')),
                ('mana_email', models.EmailField(max_length=254, verbose_name='Email\u5730\u5740')),
                ('mana_group', models.ForeignKey(verbose_name='\u4e1a\u52a1\u7ec4\u540d', to='vminfo.info_group')),
                ('mana_label', models.ManyToManyField(to='vminfo.info_label', verbose_name='\u4e1a\u52a1\u6807\u7b7e')),
            ],
            options={
                'verbose_name': '\u7ef4\u62a4\u8005',
                'verbose_name_plural': '\u7ef4\u62a4\u8005',
            },
        ),
        migrations.CreateModel(
            name='info_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=16, verbose_name='\u4e3b\u673a\u72b6\u6001')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u72b6\u6001',
                'verbose_name_plural': '\u4e3b\u673a\u72b6\u6001',
            },
        ),
        migrations.CreateModel(
            name='vm_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=32, null=True, verbose_name='\u4e3b\u673a\u540d')),
                ('os_version', models.CharField(max_length=32, null=True, verbose_name='OS\u7248\u672c')),
                ('lan_ipaddr', models.IPAddressField(null=True, verbose_name='\u5185\u7f51IP')),
                ('machine_id', models.CharField(max_length=32, null=True, verbose_name='\u4e3b\u673aID')),
                ('vm_mem', models.CharField(max_length=12, null=True, verbose_name='\u5185\u5b58')),
                ('vm_disk', models.CharField(max_length=12, null=True, verbose_name='\u786c\u76d8')),
                ('vm_cpu', models.CharField(max_length=12, null=True, verbose_name='CPU')),
                ('vm_types', models.CharField(max_length=12, null=True, verbose_name='\u4e3b\u673a\u7c7b\u578b')),
                ('vm_remark', models.TextField(max_length=256, null=True, verbose_name='\u5907\u6ce8\u4fe1\u606f')),
                ('vm_label', models.ManyToManyField(to='vminfo.info_label', verbose_name='\u4e1a\u52a1\u6807\u7b7e')),
                ('vm_location', models.ForeignKey(verbose_name='\u653e\u7f6e\u4f4d\u7f6e', to='vminfo.info_location')),
                ('vm_manager', models.ManyToManyField(to='vminfo.info_manager', verbose_name='\u7ef4\u62a4\u8005')),
                ('vm_status', models.ForeignKey(verbose_name='\u4e3b\u673a\u72b6\u6001', to='vminfo.info_status')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u4fe1\u606f',
                'verbose_name_plural': '\u4e3b\u673a\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='app_info',
            name='app_alarm',
            field=models.ManyToManyField(to='vminfo.app_info_alarm', verbose_name='\u62a5\u8b66\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='app_info',
            name='app_label',
            field=models.ForeignKey(verbose_name='\u4e1a\u52a1\u6807\u7b7e', to='vminfo.info_label'),
        ),
        migrations.AddField(
            model_name='app_info',
            name='app_manager',
            field=models.ManyToManyField(to='vminfo.info_manager', verbose_name='\u7ef4\u62a4\u8005'),
        ),
    ]
