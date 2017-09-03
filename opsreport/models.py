# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin


'''

OPS 运维报告 模型
流量
资源变更
业务报告

'''

class idc_netflow(models.Model):
	idc_name = models.CharField(u'流量接口名称', max_length = 32, blank = True)
	date_time = models.DateTimeField(u'日期时间', auto_now=False)
	flow_type = models.CharField(u'流量入出', max_length = 2, blank = True)
	flow_value = models.DecimalField(u'流量值', max_digits=7,decimal_places=2, blank = True, null = True)
	def __unicode__(self):
		return self.idc_name

	class Meta:
		verbose_name = verbose_name_plural = u'数据流量记录'
		db_table = 'idc_netflow'