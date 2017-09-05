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
#@login_required(login_url='/login/')
def index(request):
	username = request.COOKIES.get('username', '')
	##获取概览数据
	
#####数据中心 类型统计-------------------------------------------------------
	idc_types_list = idc_types.objects.all()
	idc_count = idc_info.objects.all().count()
	idc_label_count = {}
	#i = 1
	for itl in idc_types_list:
	#	idc_label_count.update({i :{}})
		idc_label_count[itl.name] = idc_info.objects.filter(types_name_id=int(itl.id)).count()
	#	i = i + 1

	##遍历idc_label_count 数据类型和类型统计数 弃用
	idc_label = []
	idc_types_count = []

	for itc in idc_types_list:
		idc_label.append(itc.name)
		idc_types_count.append(idc_info.objects.filter(types_name_id=int(itc.id)).count())

#####设备汇总 类型统计-------------------------------------------------------
	dev_types_list = device_type.objects.all()
	dev_count = device_info.objects.all().count()
	dev_label_count = {}

	for dtl in dev_types_list:
		dev_label_count[dtl.name] = device_info.objects.filter(types_id=int(dtl.id)).count()

	##遍历dev_label_count 数据类型和类型统计数 弃用
	dev_label = []
	dev_types_count = []

	for dtc in dev_types_list:
		dev_label.append(dtc.name)
		dev_types_count.append(device_info.objects.filter(types_id=int(dtc.id)).count())


#####主机汇总 类型统计-------------------------------------------------------
	host_types_list = host_info.objects.values('vm_types').distinct()
	host_count = host_info.objects.all().count()
	host_label_count = {}
	host_label = []
	host_types_count = []

	for htl in host_types_list:
		name_types = htl['vm_types']
		host_label_count[name_types] = host_info.objects.filter(vm_types=name_types).count()
	##遍历host_label_count 数据类型和类型统计数 弃用
		host_label.append(name_types)
		host_types_count.append(host_info.objects.filter(vm_types=name_types).count())

#####项目汇总 类型统计 多为柱状图需要列表，字典组合形式实现 格式如下示例
	label_types_list = info_label.objects.all()
	label_all_count = info_label.objects.all().count()
	data_host = []
	data_cpu = []
	data_app = []
	for ltl in label_types_list:
		cpu_list = []
		app_list = []
		host_list = []
		name = str(ltl)
		name_host = host_info.objects.filter(vm_label=int(ltl.id)).count()
		name_app = app_info.objects.filter(app_label_id=ltl.id).count()
		vm_cpu = []
		cpu_count = host_info.objects.filter(vm_label=int(ltl.id))
		for vcpu in cpu_count:
			vm_cpu.append(int(vcpu.vm_cpu))
		host_list.append(str(name))
		host_list.append(name_host)
		cpu_list.append(str(name))
		cpu_list.append((sum(vm_cpu)))
		app_list.append(str(name))
		app_list.append(name_app)
		data_host.append(host_list)
		data_cpu.append(cpu_list)
		data_app.append(app_list)
		data_label=[{'data': data_host, 'name': 'host'}, {'data':data_cpu, 'name': 'CPU'}, {'data': data_app, 'name': 'APP'}]
		data_goals=[{'data': idc_label_count, 'name': u'数据中心'},{'data': dev_label_count, 'name': u'设备汇总'},{'data': host_label_count, 'name': u'主机汇总'}, ]

####测试数据
	Tline=[
  [u"大头无线", "2006-06-01", "2011-07-01"],
  [u"酷六网", "2011-07-03", "2013-01-01"],
  [u"爱康国宾", "2013-01-03", "2016-01-01"],
  [u"爱接力", "2016-01-03", "2017-07-03"],
  [u"国信优易", "2017-07-05", "2017-09-01"],
  ]
	#data = {'Chrome': 52.9, 'Opera': 1.6, 'Firefox': 27.7}
	data = [{'data': [[u'项目1', 52.9], ['项目2', 50.7]], 'name': u'物理机'},
 {'data': [[u'项目1', 27.7], ['项目2', 25.9]], 'name': u'虚拟机'}]
	value = [{'data':[['2013-04-01 00:09:00 UTC',20],['2013-04-01 00:10:00 UTC',5],['2013-04-01 00:11:00 UTC',25],['2013-04-01 00:12:00 UTC',50],['2013-04-01 00:13:00 UTC',10],['2013-04-01 00:14:00 UTC',15],['2013-04-01 00:15:00 UTC',35]],'name':'Chrome'}]
##################
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
		'idc_label_count' : idc_label_count,
		'dev_label_count' : dev_label_count,
		'host_label_count' : host_label_count,
		'data_goals' : data_goals,
		'idc_count' : idc_count,
		'dev_count' : dev_count,
		'host_count' : host_count,
		'label_all_count' : label_all_count,
		'data_label' : data_label,
		'username' : username,
		'data' : data,
		'value' : value,
		'Tline' : Tline,
		},processors=[index_list])
	return HttpResponse(template.render(context))


'''
下面未测试代码部分
'''

###

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

