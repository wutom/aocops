# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

###idc models
from idcinfo.models import idc_contact, idc_types, idc_info, cabinet_info, device_type, device_info
from index.models import aocops_fileImage, aocops_indexType, aocops_indexList, aocops_indexBulletin
from vminfo.models import app_info, host_info
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


###IDC 列表视图
def idc_list(request):
	Idc_Info = idc_info.objects.all()
	icd = {}
	i = 1
	for ic in Idc_Info:
		icd.update({i :{}})
		icd[i]["idc_name"] = ic.idc_name
		icd[i]["belong"] = ic.belong
		icd[i]["location"] = ic.location
		icd[i]["contacts"] = ic.contacts.first()
		icd[i]["types_name"] = ic.types_name

		i = i + 1
	template = loader.get_template('idcinfo/idc.html')
	context = RequestContext(request,{
		'ic' : icd,
		},processors=[index_list])
	return HttpResponse(template.render(context))



###机柜 列表视图
'''
根据URL传递的id查询到数据中心所有的机柜列表
在根据机柜列表的id 去查询每个机柜里面的所有主机列表
使用到列表和字典传递需要的值到视图中
'''
def cabinet_list(request, id):
	idc_name = idc_info.objects.get(id=int(id))
	cabinets = cabinet_info.objects.filter(belong_idc=int(id)).order_by('name')
	cab_count = cabinets.count()
	
	dev_count = 0
	cids = []
	cabinet_list = []
	dev_list = {}
	
###机柜列表视图
	for cb in cabinets:
		cids.append(int(cb.id))

		cabinet_list.append({
			'id' : int(cb.id),
			'name' : cb.name,
			'remark' : cb.remark,
			})
		dev_list.update({ int(cb.id) : [] })

####每个机柜中主机列表视图
	device = device_info.objects.filter(cabinet_id__in= tuple(cids)).order_by("loc")
	for dv in device:
		dev_list[int(dv.cabinet_id)].append({
			'id' : int(dv.id),
			'order' : dv.loc,
			'name' : dv.name,
			'ip1' : dv.ipaddr1,
			'ip2' : dv.ipaddr2,
			'label' : dv.label,
			'user' : dv.user,
			})
		dev_count = dev_count + 1

	template = loader.get_template('idcinfo/cabinet_list.html')
	context = RequestContext(request,{
		'cids' : cids,
		'idc_name' : idc_name,
		'cabinet_list' : cabinet_list,
		'dev_list' : sort_dict(dev_list),
		'cab_count' : len(cids),
		'dev_count' : dev_count,
		},processors=[index_list])
	return HttpResponse(template.render(context))


###自定义函数
def sort_dict(dt):
	new_dict = {}
	for i in dt:
		new_dict.update({ i : [] })
		new_dict[i] = sorted(dt[i], key = lambda k: k['order'])
	return new_dict


###设备展示视图

def device(request, id):
	device = device_info.objects.get(id=int(id))
	dev_name = device.name
	dev_plant = device.plant_no
	dev_sn = device.sn
	dev_cabinet = device.cabinet
	dev_spec = device.spec
	dev_types = device.types
	dev_loc = device.loc
	dev_user = device.user
	dev_label = device.label
	dev_cpu = device.cpu
	dev_mem = device.mem
	dev_disk = device.disk
	dev_ip1 = device.ipaddr1
	dev_ip2 = device.ipaddr2
	dev_sys = device.system
	dev_remark = device.remark

	template = loader.get_template('idcinfo/device.html')
	context = RequestContext(request,{
		'dev_name' : dev_name,
		'dev_plant' : dev_plant,
		'dev_sn' : dev_sn,
		'dev_cabinet' : dev_cabinet,
		'dev_spec' : dev_spec,
		'dev_types' : dev_types,
		'dev_loc' : dev_loc,
		'dev_user' : dev_user,
		'dev_label' : dev_label,
		'dev_cpu' : dev_cpu,
		'dev_mem' : dev_mem,
		'dev_disk' : dev_disk,
		'dev_ip1' : dev_ip1,
		'dev_ip2' : dev_ip2,
		'dev_sys' : dev_sys,
		'dev_remark' : dev_remark,
		},processors=[index_list])
	return HttpResponse(template.render(context))
