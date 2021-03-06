# -*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin
import os
##加载vmset数据库表
from vmset.models import info_label, info_status, info_manager, info_group, app_info_alarm
from idcinfo.models import cabinet_info

#主机信息和应用程序信息
#程序信息
class app_info(models.Model):
    app_name = models.CharField(u'程序名称', max_length=20, null=True)
    hostname = models.CharField(u'主机名称', max_length=24,null=True)
    app_listen = models.CharField('程序监听', max_length=16, null=True)
    app_pid = models.IntegerField(u'程序PID', null=True)
    app_vm_id = models.IntegerField(u'主机ID', max_length=42, null=True)
    app_id = models.CharField(u'程序ID', max_length=20, null=True)
    app_label = models.ForeignKey(info_label, verbose_name=u'业务标签', blank = True, null=True)
    app_manager = models.ManyToManyField(info_manager, verbose_name=u'维护者', blank = True, null=True)
    app_alarm = models.ManyToManyField(app_info_alarm, verbose_name=u'报警类型', blank = True, null=True)
    app_remark = models.TextField(u'备注信息', max_length=256, blank = True, null=True)

    def __unicode__(self):
        return self.app_name
    class Meta:
        verbose_name = verbose_name_plural = u'程序信息'
        db_table = 'vminfo_app_info'
#主机信息
class host_info(models.Model):
    hostname = models.CharField(u'主机名', max_length=32, null = True)
    os_version = models.CharField(u'OS版本', max_length=32, null = True)
    lan_ipaddr = models.GenericIPAddressField(u'内网IP', max_length=16,null = True)
    machine_id = models.CharField(u'主机ID', max_length=42, null = True)
    vm_mem = models.IntegerField(u'内存', null = True)
    vm_disk = models.IntegerField(u'系统盘', null = True)
    vm_cpu = models.IntegerField(u'CPU', null = True)
    vm_types = models.CharField(u'主机类型', max_length=12, null = True)
    vm_location = models.ForeignKey(cabinet_info, verbose_name = u'放置位置', blank = True, null=True)
    vm_label = models.ForeignKey(info_label, verbose_name=u'业务标签', blank = True, null=True)
    vm_status = models.ForeignKey(info_status, verbose_name=u'主机状态', blank = True, null = True)
    vm_manage = models.ManyToManyField(info_manager, verbose_name=u'维护者', blank = True, null = True)
    vm_remark = models.TextField(u'备注信息', max_length=256, blank = True, null = True)

    def __unicode__(self):
        return self.hostname

    class Meta:
        verbose_name = verbose_name_plural = u'主机信息'
        db_table = 'vminfo_host_info'

