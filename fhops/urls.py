# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'login.views.login'),
    url(r'^logout/', 'login.views.logout'),
    ##首页
    url(r'^$', 'index.views.index'),
    ##IDC
    url(r'^idcinfo/', 'index.views.idc_list'),
    url(r'^cabinet/(?P<id>\d+)/$', 'index.views.cabinet_list'),
    url(r'^device/(?P<id>\d+)/$', 'index.views.device'),
    url(r'^host/(?P<id>\d+)/$', 'idcinfo.views.host_app'),
    #url(r'^cabinet/test/', 'index.views.cabinet_list'),
    ##其它个页面
    url(r'^hostinfo/', 'index.views.hostinfo'),
    url(r'^appinfo/', 'index.views.appinfo'),

]

