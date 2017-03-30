# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models
from idcinfo.models import idc_contact, idc_info, cabinet_info, device_type, device_info, idc_types


# admin 后台管理页面的显示栏目信息
class idc_info_admin(admin.ModelAdmin):
	formfield_overrides = {
		models.ManyToManyField: {'widget': CheckboxSelectMultiple},
	}

	list_display = ('idc_name', 'belong', 'location', 'contact_names', 'types_name', 'remark')
	search_fields = ['idc_name', 'location', 'belong__belong_name', 'contacts__contact_name', 'remark']
	list_per_page = 50
	ordering = ('id',)

class idc_types_admin(admin.ModelAdmin):
	list_display = ('name', 'remark')
	list_per_page = 50
	ordering = ('id',)


class idc_contact_admin(admin.ModelAdmin):
	list_display = ('contact_name', 'phone', 'remark')
	search_fields = ['contact_name', 'phone', 'remark']
	list_per_page = 50
	ordering = ('id',)

class cabinet_info_admin(admin.ModelAdmin):
	list_display = ('name', 'belong_idc', 'location', 'remark')
	search_fields = ['name', 'belong_idc__idc_name', 'location', 'remark']
	list_per_page = 50
	ordering = ['belong_idc', 'name', ]

class device_type_admin(admin.ModelAdmin):
	list_display = ('name', 'remark')
	search_fields = ['name', 'remark']
	list_per_page = 50
	ordering = ['id', ]

class device_info_admin(admin.ModelAdmin):
	list_display = ('name', 'cabinet', 'spec', 'ipaddr1', 'ipaddr2', 'user', 'system')
	search_fields = ['name', 'sn', 'cabinet__name', 'cabinet__belong_idc__idc_name',
		'mem', 'cpu', 'disk', 'spec', 'ipaddr1', 'ipaddr2', 'ctrl_ip', 'user', 'system']
	list_per_page = 50
	ordering = ['id', ]


##注册模型到admin管理后台

admin.site.register(idc_contact, idc_contact_admin)
admin.site.register(idc_info, idc_info_admin)
admin.site.register(idc_types, idc_types_admin)
admin.site.register(cabinet_info, cabinet_info_admin)
admin.site.register(device_type, device_type_admin)
admin.site.register(device_info, device_info_admin)