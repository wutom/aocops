# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
import os
from datetime import datetime, timedelta
from django.db.models.fields.files import ImageFieldFile
OK = 1

class aocops_indexBulletin(models.Model):
    Bull_name = models.CharField(u'公告标题', max_length=20, null=True)
    Bull_remark = models.TextField(u'文档备注', max_length=256, blank = True, null = True)
    def __unicode__(self):
        return self.Bull_name

    class Meta:
        verbose_name = verbose_name_plural = u'公司公告'
        db_table = 'index_aocops_indexBulletin'

class aocops_fileImage(models.Model):
    fi_name = models.CharField(u'文档标题', max_length=20, null = True)
    fi_image = models.FileField(u'文档路径', upload_to='img/', null = True, blank = True)
    fi_remark = models.TextField(u'文档备注', max_length=256, blank = True, null = True)

    def __unicode__(self):
        return self.fi_name

    class Meta:
        verbose_name = verbose_name_plural = u'公司文档'
        db_table = 'index_aocops_fileimage'
#        if OK == 1:
#            app_label = u'index'


class aocops_indexType(models.Model):
    it_name = models.CharField(u'导航分类', max_length = 20)
    it_remark = models.TextField(u'分类备注',max_length=256, null = True, blank = True)

    def __unicode__(self):
        return self.it_name

    class Meta:
        verbose_name = verbose_name_plural = u'导航分类' 
        db_table = 'index_aocops_indextype'
#        if OK == 1:
#            app_lable = u'index'

class aocops_indexList(models.Model):
    il_name = models.CharField(u'导航名称', max_length=20,)
    types = models.ForeignKey(aocops_indexType, verbose_name = u'导航分类')
    il_url = models.CharField(u'导航地址', max_length=100, null = True, blank = True)
    il_remark = models.TextField(u'导航备注', max_length=256, blank = True, null = True)

    def __unicode__(self):
        return self.il_name

    class Meta:
        verbose_name = verbose_name_plural = u'导航管理'
        db_table = 'index_aocops_indexlist'
#        if OK == 1:
#            app_label = u'index'
