# -*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin
import os

#主机信息和应用程序信息
#业务标签
class info_label(models.Model):
    label = models.CharField(u'业务标签', max_length=16)
    def __unicode__(self):
        return self.label
    class Meta:
        verbose_name = verbose_name_plural = u'业务标签'
#主机状态
class info_status(models.Model):
    status = models.CharField(u'主机状态', max_length=16)
    def __unicode__(self):
        return self.status
    class Meta:
        verbose_name = verbose_name_plural = u'主机状态'

class info_group(models.Model):
    group_name = models.CharField(u'业务组名', max_length=16, null=True)
    def __unicode__(self):
        return self.group_name
    class Meta:
        verbose_name = verbose_name_plural = u'业务组名'

class app_info_alarm(models.Model):
    alarm_types = models.CharField(u'报警类型', max_length=10, null=True)

    def __unicode__(self):
        return self.alarm_types
    class Meta:
        verbose_name = verbose_name_plural = u'报警类型'


#维护者信息
class info_manager(models.Model):
    mana_name = models.CharField(u'维护者姓名', max_length=12, null=True)
    mana_phone = models.CharField(u'维护者电话', max_length=12, null=True)
    mana_email = models.EmailField(u'Email地址',)
    mana_group = models.ForeignKey(info_group,verbose_name=u'业务组名')
    mana_label = models.ManyToManyField(info_label,verbose_name=u'业务标签')
    def __unicode__(self):
        return self.mana_name

    class Meta:
        verbose_name = verbose_name_plural = u'维护者'
