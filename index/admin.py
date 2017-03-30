# -*- coding: utf-8 -*-
from django.contrib import admin
from index.models import aocops_fileImage, aocops_indexList, aocops_indexType, aocops_indexBulletin

#首页公告

class admin_aocops_indexBulletin(admin.ModelAdmin):
    list_display = ('Bull_name','Bull_remark')

#首页文档
class admin_aocops_fileImage(admin.ModelAdmin):
    list_display = ('fi_name', 'fi_image', 'fi_remark')
    search_fields = ['fi_name']
    list_per_page = 50
    ordering = ['id',]

#首页导航
class admin_aocops_indexList(admin.ModelAdmin):
    list_display = ('il_name', 'il_url', 'il_remark')
    search_fields = ['il_name']
    list_per_page = 50
    ordering = ['id',]

#导航分类
class admin_aocops_indexType(admin.ModelAdmin):
    list_display = ('it_name', 'it_remark')
    list_per_page = 50
    ordering = ['id',]


admin.site.register(aocops_indexBulletin,admin_aocops_indexBulletin)
admin.site.register(aocops_fileImage,admin_aocops_fileImage)
admin.site.register(aocops_indexList,admin_aocops_indexList)
admin.site.register(aocops_indexType,admin_aocops_indexType)
