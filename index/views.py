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

#####项目汇总 类型统计
	label_types_list = info_label.objects.all()
	label_all_count = info_label.objects.all().count()
	label_count = {}

	for ltl in label_types_list:
		name_label = str(ltl)
		label_count[name_label] = host_info.objects.filter(vm_label=int(ltl.id)).count()

####测试数据
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
		'idc_count' : idc_count,
		'dev_count' : dev_count,
		'host_count' : host_count,
		'label_count' :label_count,
		'label_all_count' : label_all_count,
		'username' : username,
		'data' : data,
		'value' : value,
		},processors=[index_list])
	return HttpResponse(template.render(context))
	
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

	template = loader.get_template('index/hostinfo.html')
	context = RequestContext(request,{
		'lih' : lih,
		'lhp' : lhp,
		'host_count' : host_count,
		'host_label_count' : host_label_count,
		},processors=[index_list])
	return HttpResponse(template.render(context))

#@login_required(login_url='/login/')
def appinfo(request):
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

	template = loader.get_template('index/appinfo.html')
	context = RequestContext(request,{
		'lia' : lia,
		'lap' : lap
		},processors=[index_list])
	return HttpResponse(template.render(context))


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

