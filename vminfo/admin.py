# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from vminfo.models import host_info, app_info


#主机信息
class host_vm_info(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
        }
    list_display = ('hostname', 'lan_ipaddr', 'os_version', 'vm_mem', 'vm_disk', 'vm_cpu', 'vm_types', 'vm_location', 'vm_status')
    search_fields = ['machine_id', 'lan_ipaddr']
    list_per_page = 50
    ordering = ['id',]
#程序信息
class vmapp_info(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
        }
    list_display = ('app_name','hostname', 'app_listen', 'app_pid', 'app_label')
    search_fields = ['app_name']
    list_per_page = 50
    ordering = ['id',]



admin.site.register(app_info,vmapp_info)
admin.site.register(host_info,host_vm_info)
