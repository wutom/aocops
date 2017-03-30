# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
import os
from datetime import datetime, timedelta
from django.db.models.fields.files import ImageFieldFile
OK = 1

class Article(models.Model):
    Bull_name = models.CharField(u'公告标题', max_length=20, null=True)
    Bull_remark = models.TextField(u'文档备注', max_length=256, blank = True, null = True)
    def __unicode__(self):
        return self.Bull_name

    class Meta:
        verbose_name = verbose_name_plural = u'公司公告'
        db_table = 'index_aocops_indexBulletin'