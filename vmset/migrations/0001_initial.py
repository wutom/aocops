# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
                ('mana_group', models.ForeignKey(verbose_name='\u4e1a\u52a1\u7ec4\u540d', to='vmset.info_group')),
                ('mana_label', models.ManyToManyField(to='vmset.info_label', verbose_name='\u4e1a\u52a1\u6807\u7b7e')),
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
    ]
