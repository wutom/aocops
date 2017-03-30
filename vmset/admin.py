# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from vmset.models import info_label, info_location, info_status, info_manager, info_group, app_info_alarm

#主机类型
class vminfo_label(admin.ModelAdmin):
    list_display = [('label')]
    list_per_page = 50
    ordering = ['id',]

class vminfo_location(admin.ModelAdmin):
    list_display = [('location')]
    list_per_page = 50
    ordering = ['id',]

class vminfo_status(admin.ModelAdmin):
    list_display = [('status')]
    list_per_page = 50
    ordering = ['id',]

class vmapp_info_alarm(admin.ModelAdmin):
    list_display = [('alarm_types')]
    list_per_page = 50
    ordering = ['id',]

class vminfo_manager(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
        }
    list_display = ('mana_name','mana_phone','mana_email','mana_group')
    list_per_page = 50
    ordering = ['id',]

class vminfo_group(admin.ModelAdmin):
    list_display = [('group_name')]
    list_per_page = 50
    ordering = ['id',]


admin.site.register(info_label,vminfo_label)
admin.site.register(info_location,vminfo_location)
admin.site.register(info_status,vminfo_status)
admin.site.register(info_manager,vminfo_manager)
admin.site.register(info_group,vminfo_group)
admin.site.register(app_info_alarm,vmapp_info_alarm)