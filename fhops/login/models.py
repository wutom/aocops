# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

##认证方式基于django管理后台用户，本models暂时弃用
##2017-06-26
# Create your models here.

class user_ldap_mail_mobile(models.Model):
	ldap = models.CharField(u'LDAP用户名', max_length = 24)
	email = models.CharField(u'Email', max_length = 24)
	mobile = models.CharField(u'电话号码', max_length = 11)


	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name = verbose_name_plural = u'员工列表'
		db_table = 'userlm'