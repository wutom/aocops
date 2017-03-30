# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from vminfo.models import host_info, app_info
#首页视图
# Create your views here.
import time, re
from django.contrib import admin
from django.template import Context, loader
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.utils.html import strip_spaces_between_tags as short  # drop empty line
from django.utils.encoding import smart_str
from django.utils.http import urlquote
from django.db.models import Q

#导航栏部分

def host_info(request):
	lhost = host_info.objects.all().order_by('hostname')
	server = request.META['HTTP_HOST']
	##定义空值导入数据库数值
	lih = {}
	i = 1
	for lh in lhost:
		lih.update({i : {}})
		lih[i]["lh_hostname"] = lh.hostname
		lih[i]["lan_ipaddr"] = lh.lan_ipaddr
		lih[i]["os_version"] = lh.os_version
		lih[i]["vm_cpu"] = lh.vm_cpu
		lih[i]["vm_disk"] = lh.vm_disk
		lih[i]["vm_mem"] = lh.vm_mem
		lih[i]["vm_types"] = lh.vm_types
		lih[i]["vm_location"] = lh.vm_location
		lih[i]["vm_status"] = lh.vm_status
		lih[i]["vm_manage"] = lh.vm_manage
		lih[i]["machine_id"] = lh.machine_id

		i = i + 1

	template = loader.get_template('index/hostinfo.html')
	context = Context({
		'lih' : lih,
		'server' : server
		})
	return HttpResponse(short(template.render(context)))