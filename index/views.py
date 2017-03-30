# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
###app models
from index.models import aocops_fileImage, aocops_indexType, aocops_indexList, aocops_indexBulletin
from vminfo.models import host_info, app_info
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

#导航栏部分已全局变量的方式返回给具体视图

def index_list(request):
	#获取导航分类id和分类名称
	list_types = aocops_indexType.objects.all().order_by('it_name')
	#定义主机地址
	server = request.META['HTTP_HOST']
	img_serve = "c.ops.com"
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

##视图全局变量测试函数,需要具体视图引用
def glob(request):
	context = {'glo': 'glo'}
	return context
'''
引用示例
def index(request):
	bull = aocops_indexBulletin.objects.all()
	bul = {}
	i = 1
	for bl in bull:
		bul.update({i : {}})
		bul[i]["bl_name"] = bl.Bull_name
		bul[i]["bl_remark"] = bl.Bull_remark
		i = i + 1

	template = loader.get_template('index/index.html')
	context = RequestContext(request,{
		'bul' : bul
		},processors=[glob])
	return HttpResponse(template.render(context))

'''
@login_required(login_url='/login/')
def index(request):
	username = request.COOKIES.get('username', '')
	##获取概览数据
	##数据中心-IDC
	#公有云
	cidc =  idc_info.objects.filter(types_name_id=1).count()
	#物理机房
	iidc =  idc_info.objects.filter(types_name_id=2).count()
	#私有云
	pidc =  idc_info.objects.filter(types_name_id=3).count()

	##平台汇总
	ail = aocops_indexList.objects.all().count() 
	##程序汇总 
	aif = app_info.objects.all().count()
	##设备汇总
	dif = device_info.objects.all().count()
	##主机汇总
	hif = host_info.objects.all().count()
	bull = aocops_indexBulletin.objects.all()
	bul = {}
	i = 1
	for bl in bull:
		bul.update({i : {}})
		bul[i]["bl_name"] = bl.Bull_name
		bul[i]["bl_remark"] = bl.Bull_remark
		i = i + 1

	template = loader.get_template('index/index.html')
	context = RequestContext(request,{
		'bul' : bul,
		'cidc' : cidc,
		'iidc' : iidc,
		'pidc' : pidc,
		'ail' : ail,
		'aif' : aif,
		'dif' : dif,
		'hif' : hif,
		'username' : username
		},processors=[index_list])
	return HttpResponse(template.render(context))
	
@login_required(login_url='/login/')
def hostinfo(request):
	limit = 20
	list_host = host_info.objects.all()
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

	template = loader.get_template('index/hostinfo.html')
	context = RequestContext(request,{
		'lih' : lih,
		'lhp' : lhp,
		},processors=[index_list])
	return HttpResponse(template.render(context))

@login_required(login_url='/login/')
def appinfo(request):
	limit = 20
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

	template = loader.get_template('index/appinfo.html')
	context = RequestContext(request,{
		'lia' : lia,
		'lap' : lap
		},processors=[index_list])
	return HttpResponse(template.render(context))

## 获取请求数据
def dnsfind(request):
    return render_to_response('index/dnsfind.html')
 
## 接收请求数据
def search(request):  
    ctx = {}
    if request.method == "GET":
    	ctx['domain'] = request.GET['domain']
    	ctx['dnsip'] = request.GET['dnsip']
    	cmdd="python /opt/aocdev/aocops/index/dnsfind.py %s %s" % (ctx['domain'], ctx['dnsip'])
    	dns=os.popen(cmdd).read()
    template = loader.get_template('index/search.html')
    dn = {'dns':dns} 
    #return HttpResponse(template.render(dn))
    return HttpResponse(dns)

