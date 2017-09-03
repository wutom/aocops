# -*- coding: utf-8 -*-
from django.contrib import admin
from opsreport.models import idc_netflow


#OPS 流量报告
class admin_opsreport_flow(admin.ModelAdmin):
    list_display = ('date_time', 'flow_type', 'flow_value', 'idc_name')
    search_fields = ['idc_name',]
    list_per_page = 50
    ordering = ['id',]

admin.site.register(idc_netflow,admin_opsreport_flow)