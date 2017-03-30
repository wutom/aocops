# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aocops_fileImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fi_name', models.CharField(max_length=20, null=True, verbose_name='\u6587\u6863\u6807\u9898')),
                ('fi_image', models.FileField(upload_to=b'img/', null=True, verbose_name='\u6587\u6863\u8def\u5f84', blank=True)),
                ('fi_remark', models.TextField(max_length=256, null=True, verbose_name='\u6587\u6863\u5907\u6ce8', blank=True)),
            ],
            options={
                'db_table': 'index_aocops_fileimage',
                'verbose_name': '\u516c\u53f8\u6587\u6863',
                'verbose_name_plural': '\u516c\u53f8\u6587\u6863',
            },
        ),
        migrations.CreateModel(
            name='aocops_indexList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('il_name', models.CharField(max_length=20, verbose_name='\u5bfc\u822a\u540d\u79f0')),
                ('il_url', models.CharField(max_length=100, null=True, verbose_name='\u5bfc\u822a\u5730\u5740', blank=True)),
                ('il_remark', models.TextField(max_length=256, null=True, verbose_name='\u5bfc\u822a\u5907\u6ce8', blank=True)),
            ],
            options={
                'db_table': 'index_aocops_indexlist',
                'verbose_name': '\u5bfc\u822a\u7ba1\u7406',
                'verbose_name_plural': '\u5bfc\u822a\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='aocops_indexType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('it_name', models.CharField(max_length=20, verbose_name='\u5bfc\u822a\u5206\u7c7b')),
                ('it_remark', models.TextField(max_length=256, null=True, verbose_name='', blank=True)),
            ],
            options={
                'db_table': 'index_aocops_indextype',
                'verbose_name': '\u5bfc\u822a\u5206\u7c7b',
                'verbose_name_plural': '\u5bfc\u822a\u5206\u7c7b',
            },
        ),
        migrations.AddField(
            model_name='aocops_indexlist',
            name='types',
            field=models.ForeignKey(verbose_name='\u5bfc\u822a\u5206\u7c7b', to='index.aocops_indexType'),
        ),
    ]
