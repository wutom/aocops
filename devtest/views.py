# -*- coding:utf-8 -*-
from django import forms
from django.http import HttpResponseRedirect
import os, sys
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

####
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
from index.views import index_list
# Create your views here.


def hostinfo(request):
	limit = 10 #每页显示的记录数
	list_host = host_info.objects.all() #获取数据库值
	paginator = Paginator(list_host, limit) #实例化分页
	page = request.GET.get('page') #获取页码，在模板中获取page值

	try:
		lhp = paginator.page(page) #page页
	except PageNotAnInteger:
		lhp = paginator.page(1)  #如果页码不是整数，获取第一页
	except EmptyPage:
		lhp = paginator.page(paginator.num_pages) #如果页码太大获取最后一页
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
	template = loader.get_template('index/hostinfo_p.html')
	context = RequestContext(request,{
		'lih' : lih, #具体值
		'lhp' : lhp, #页码值 模板需要调用
		},processors=[index_list])
	return HttpResponse(template.render(context))


class ArticleForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20)


def create(request):
	ctx = {}
	if request.method == 'POST':
		ctx['domain'] = request.POST['domain']
		ctx['dnsip'] = request.POST['dnsip']
		cmdd="python /opt/aocdev/aocops/index/dnsfind.py %s %s" % (ctx['domain'], ctx['dnsip'])
		
		a=os.popen(cmdd).read()

	return render(request, "index/dnsfind.html", a)


