# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vminfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='host_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=32, null=True, verbose_name='\u4e3b\u673a\u540d')),
                ('os_version', models.CharField(max_length=32, null=True, verbose_name='OS\u7248\u672c')),
                ('lan_ipaddr', models.GenericIPAddressField(null=True, verbose_name='\u5185\u7f51IP')),
                ('machine_id', models.IntegerField(max_length=16, null=True, verbose_name='\u4e3b\u673aID')),
                ('vm_mem', models.IntegerField(max_length=6, null=True, verbose_name='\u5185\u5b58')),
                ('vm_disk', models.CharField(max_length=32, null=True, verbose_name='\u5206\u533a')),
                ('vm_cpu', models.IntegerField(max_length=6, null=True, verbose_name='CPU')),
                ('vm_location', models.CharField(max_length=12, null=True, verbose_name='\u653e\u7f6e\u4f4d\u7f6e')),
                ('vm_types', models.CharField(max_length=12, null=True, verbose_name='\u4e3b\u673a\u7c7b\u578b')),
                ('vm_remark', models.TextField(max_length=256, null=True, verbose_name='\u5907\u6ce8\u4fe1\u606f')),
                ('vm_label', models.ManyToManyField(to='vminfo.info_label', verbose_name='\u4e1a\u52a1\u6807\u7b7e')),
                ('vm_manager', models.ManyToManyField(to='vminfo.info_manager', verbose_name='\u7ef4\u62a4\u8005')),
                ('vm_status', models.ForeignKey(verbose_name='\u4e3b\u673a\u72b6\u6001', to='vminfo.info_status')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u8be6\u60c5',
                'verbose_name_plural': '\u4e3b\u673a\u8be6\u60c5',
            },
        ),
        migrations.AlterField(
            model_name='vm_info',
            name='lan_ipaddr',
            field=models.GenericIPAddressField(null=True, verbose_name='\u5185\u7f51IP'),
        ),
    ]
