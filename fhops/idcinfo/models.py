# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from vmset.models import info_manager, info_label
 

OK = 1
MAX_DEV_PER_CABINET = 100
# Create your models here.

'''
##IDC基本信息
'''

class idc_contact(models.Model):
	contact_name = models.CharField(u'联系人', max_length = 128)
	phone = models.CharField(u'电话', max_length = 64)
	remark = models.TextField(u'备注', max_length = 256, blank = True, null = True)

	def __unicode__(self):
		return self.contact_name
	
	class Meta:
		verbose_name = verbose_name_plural = u'数据中心联系人'
		db_table = 'idc_contact'

class idc_types(models.Model):
	name = models.CharField(u'数据中心类型', max_length = 12)
	remark = models.TextField(u'备注', max_length = 256, blank = True, null = True)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = verbose_name_plural = u'IDC类型'
		db_table = 'idc_types'


class idc_info(models.Model):
	idc_name = models.CharField(u'数据中心名称', max_length = 32)
	belong = models.ForeignKey(info_manager, verbose_name = u'维护者')
	location = models.CharField(u'放置位置', max_length = 256, blank = True, null = True)
	contacts = models.ManyToManyField(idc_contact, verbose_name = u'联系人')
	types_name = models.ForeignKey(idc_types, verbose_name = u'数据中心类型')
	remark = models.TextField(u'备注', max_length = 256, blank = True, null = True)

	def __unicode__(self):
		return self.idc_name

	def contact_names(self):
		return ' '.join([u.contact_name for u in self.contacts.all()])
	
	contact_names.short_description = "联系人"

	class Meta:
		verbose_name = verbose_name_plural = u'数据中心'
		db_table = 'idc_info'

			
'''
IDC机柜机柜信息
'''

class cabinet_info(models.Model):
	name = models.CharField(u'机柜编号', max_length = 32)
	belong_idc = models.ForeignKey(idc_info, verbose_name = u'归属数据中心')
	location = models.CharField(u'机柜位置', max_length = 256, blank = True, null = True)
	remark = models.TextField(u'备注', max_length = 256, blank = True, null = True)

	def __unicode__(self):
		return self.belong_idc.idc_name + ' ' + self.name

	class Meta:
		verbose_name = verbose_name_plural = u'机柜列表'
		db_table = 'cabinet_info'


'''
IDC设备信息
'''

class device_type(models.Model):
	name = models.CharField(u'设备类型', max_length = 32)
	remark = models.TextField(u'备注', max_length = 256, blank = True, null = True)
	
	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = verbose_name_plural = u'设备类型'
		db_table = 'device_type'


class device_info(models.Model):
	SPEC_LIST = (
		('1U', '1U'),
		('2U', '2U'),
		('3U', '3U'),
		('4U', '4U'),
		('5U', '5U'),
		('VU', 'VM'),
	)
	LOC_ID = []
	for i in range(1, MAX_DEV_PER_CABINET + 1):
		LOC_ID.append((i, i))

	name = models.CharField(u'设备名称', max_length = 32)
	plant_no = models.CharField(u'唯一识别号', max_length = 64)
	sn = models.CharField(u'序列号', max_length = 32, help_text='设备的序列号')
	cabinet = models.ForeignKey(cabinet_info, verbose_name = u'机柜编号或云主机地域', help_text='可以是物理IDC机柜编号也可以是云主机地域描述')
	spec = models.CharField(u'规格尺寸', max_length = 32, choices = SPEC_LIST)
	types = models.ForeignKey(device_type, verbose_name = u'设备类型')
	loc = models.IntegerField(u'机架顺序', choices = LOC_ID, help_text='机架上的摆放顺序，从上至下，如果是云主机顺序可以随意')
	user = models.ForeignKey(info_manager, verbose_name = u'维护者', help_text='设备详细信息')
	label = models.ForeignKey(info_label, verbose_name = u'业务标签', null = True, help_text='具体业务分组或类别，例如：OPS')
	cpu = models.CharField(u'CPU', max_length = 64, blank = True, null = True)
	mem = models.CharField(u'内存', max_length = 64, blank = True, null = True)
	disk = models.CharField(u'硬盘', max_length = 128, blank = True, null = True)
	ipaddr1 = models.CharField(u'IP 地址1', max_length = 128, blank = True, null = True)
	ipaddr2 = models.CharField(u'IP 地址2', max_length = 128, blank = True, null = True)
	ipaddr3 = models.CharField(u'IP 地址3', max_length = 128, blank = True, null = True)
	ipaddr4 = models.CharField(u'IP 地址4', max_length = 128, blank = True, null = True)
	mac1 = models.CharField(u'MAC 地址1', max_length = 64, blank = True, null = True)
	mac2 = models.CharField(u'MAC 地址2', max_length = 64, blank = True, null = True)
	mac3 = models.CharField(u'MAC 地址3', max_length = 64, blank = True, null = True)
	mac4 = models.CharField(u'MAC 地址4', max_length = 64, blank = True, null = True)
	sw1 = models.CharField(u'交换机端口1', max_length = 64, blank = True, null = True)
	sw2 = models.CharField(u'交换机端口2', max_length = 64, blank = True, null = True)
	sw3 = models.CharField(u'交换机端口3', max_length = 64, blank = True, null = True)
	sw4 = models.CharField(u'交换机端口4', max_length = 64, blank = True, null = True)
	ctrl_ip = models.CharField(u'控制卡IP', max_length = 32, blank = True, null = True)
	system = models.CharField(u'操作系统类型', max_length = 64, blank = True, null = True)
	remark = models.TextField(u'备注', max_length = 256, blank = True, null = True)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = verbose_name_plural = u'设备列表'
		db_table = 'device_info'

