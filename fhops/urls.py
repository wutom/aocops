# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    ##登录部分
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'login.views.login'),
    url(r'^logout/', 'login.views.logout'),
    url(r'^reset/', 'login.views.cgp'),
    ##首页部分
    url(r'^$', 'index.views.index'),
    ##IDC部分
    url(r'^idcinfo/', 'idcinfo.views.idc_list'),
    url(r'^cabinet/(?P<id>\d+)/$', 'idcinfo.views.cabinet_list'),
    url(r'^device/(?P<id>\d+)/$', 'idcinfo.views.device'),
    
    #url(r'^cabinet/test/', 'index.views.cabinet_list'),
    ##主机和程序APP部分
    url(r'^hostinfo/', 'vminfo.views.hostinfo'),
    url(r'^host/(?P<id>\d+)/$', 'vminfo.views.host_app'),
    url(r'^appinfo/', 'vminfo.views.appinfo'),

]

