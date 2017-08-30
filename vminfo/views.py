# -*- coding:utf-8 -*-
import json
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
###app models
from index.models import aocops_fileImage, aocops_indexType, aocops_indexList, aocops_indexBulletin
from vminfo.models import host_info, app_info
from vmset.models import info_label, info_manager, info_group, info_status, app_info_alarm
from idcinfo.models import idc_contact, idc_types, idc_info, cabinet_info, device_type, device_info

#### Create your views here.
import time, re
import os, sys, subprocess
from django.views.decorators import csrf
from django.contrib import admin
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.utils.html import strip_spaces_between_tags as short  # drop empty line
from django.utils.encoding import smart_str
from django.utils.http import urlquote
from django.db.models import Q

####加载自定义模块
####弃用matplotlib 绘图，采用chartkick
#from api.python import matp

#导航栏部分已全局变量的方式返回给具体视图

def index_list(request):
	#获取导航分类id和分类名称
	list_types = aocops_indexType.objects.all().order_by('it_name')
	#定义主机地址
	server = request.META['HTTP_HOST']
	img_serve = "m.ops.com"
	list_file = aocops_fileImage.objects.all()
	##定义空值导入数据库数值
	db_types = {}
	types_items = {}
	t = 1
	fil = {}

	i = 1
	for fi in list_file:
		fil.update({i : {}})
		fil[i]["fi_name"] = fi.fi_name
		fil[i]["fi_image"] = fi.fi_image
		i = i + 1

	i = 1
	for types_var in list_types:
		db_types.update({i : {}})
		db_types[i]["it_name"] = types_var.it_name
		db_types[i]["it_id"] = types_var.id
		i = i + 1
		#获取分类id对应的具体导航名称和地址
		list_item = aocops_indexList.objects.filter(types_id=types_var.id)
		
		for items_var in list_item:
			types_items.update({t : {}})
			types_items[t]["il_name"] = items_var.il_name
			types_items[t]["il_url"] = items_var.il_url
			types_items[t]["il_id"] = items_var.types_id
			t = t + 1

	return {
		'db_types' : db_types,
		'types_items' : types_items,
		'fil' : fil,
		'server' : server,
		'img_server' : img_serve
		}


#@login_required(login_url='/login/')
def hostinfo(request):
	#####主机汇总 类型统计-------------------------------------------------------
	host_types_list = host_info.objects.values('vm_types').distinct()
	host_label_count = {}

	for htl in host_types_list:
		name_types = htl['vm_types']
		host_label_count[name_types] = host_info.objects.filter(vm_types=name_types).count()

	limit = 50
	list_host = host_info.objects.all()
	host_count = host_info.objects.all().count()
	paginator = Paginator(list_host, limit)
	page = request.GET.get('page')

	try:
		lhp = paginator.page(page)
	except PageNotAnInteger:
		lhp = paginator.page(1)
	except EmptyPage:
		lhp = paginator.page(paginator.num_pages)
	##定义空值导入数据库数值
	lih = {}
	i = 1
	for lh in lhp:
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
		lih[i]["vm_manage"] = lh.vm_manage.first()
		lih[i]["machine_id"] = lh.machine_id

		i = i + 1

	template = loader.get_template('vminfo/hostinfo.html')
	context = RequestContext(request,{
		'lih' : lih,
		'lhp' : lhp,
		'host_count' : host_count,
		'host_label_count' : host_label_count,
		},processors=[index_list])
	return HttpResponse(template.render(context))


def host_app(request, id):
	host = host_info.objects.get(id=int(id))
	app = app_info.objects.filter(app_vm_id=int(host.machine_id))
    ####主机信息
	host_name = host.hostname
	host_os = host.os_version
	host_ip = host.lan_ipaddr
	host_id = host.machine_id
	host_mem = host.vm_mem
	host_disk = host.vm_disk
	host_cpu = host.vm_cpu
	host_types = host.vm_types
	host_location = host.vm_location
	host_label = host.vm_label
	host_status = host.vm_status
	host_manager = host.vm_manage.first()

	####程序信息
	appl = {}
	i = 1
	for al in app:
		appl.update({i : {}})
		appl[i]["app_name"] = al.app_name
		appl[i]["app_label"] = al.app_label
		appl[i]["app_listen"] = al.app_listen
		appl[i]["app_id"] = al.app_id
		appl[i]["app_vm_id"] = al.app_vm_id
		appl[i]["app_manager"] = al.app_manager.first()

		i = i + 1

	template = loader.get_template('vminfo/host.html')
	context = RequestContext(request,{
		'host_name' : host_name,
		'host_os' : host_os,
		'host_ip' : host_ip,
		'host_id' : host_id,
		'host_mem' : host_mem,
		'host_disk' : host_disk,
		'host_cpu' : host_cpu,
		'host_types' : host_types,
		'host_location' : host_location,
		'host_label' : host_label,
		'host_status' : host_status,
		'host_manager' : host_manager,
		'appl' : appl,
		},processors=[index_list])
	return HttpResponse(template.render(context))


#@login_required(login_url='/login/')
def appinfo(request):
	#####APP汇总 类型统计-------------------------------------------------------
	app_count = app_info.objects.all().count()
	app_types_list = app_info.objects.values('app_name').distinct()
	app_types_count = app_info.objects.values('app_name').distinct().count()
	app_label_count = {}

	for atl in app_types_list:
		name_types = atl['app_name']
		app_label_count[name_types] = app_info.objects.filter(app_name=name_types).count()


	limit = 50
	#获取导航分类id和分类名称
	list_app = app_info.objects.all()
	paginator = Paginator(list_app, limit)
	page = request.GET.get('page')

	try:
		lap = paginator.page(page)
	except PageNotAnInteger:
		lap = paginator.page(1)
	except EmptyPage:
		lap = paginator.page(paginator.num_pages)
	##定义空值导入数据库数值
	lia = {}
	i = 1
	for la in lap:
		lia.update({i : {}})
		lia[i]["app_name"] = la.app_name
		lia[i]["hostname"] = la.hostname
		lia[i]["app_listen"] = la.app_listen
		lia[i]["app_pid"] = la.app_pid
		lia[i]["app_id"] = la.app_id
		lia[i]["app_label"] = la.app_label
		lia[i]["app_manager"] = la.app_manager.first()
		lia[i]["app_alarm"] = la.app_alarm.first()
		lia[i]["app_vm_id"] = la.app_vm_id

		i = i + 1

	template = loader.get_template('vminfo/appinfo.html')
	context = RequestContext(request,{
		'lia' : lia,
		'lap' : lap,
		'app_count' : app_count,
		'app_types_count' : app_types_count,
		'app_label_count' : app_label_count,
		},processors=[index_list])
	return HttpResponse(template.render(context))