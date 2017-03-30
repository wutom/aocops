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
    url(r'^reset/', 'login.views.reset'),
    ##首页
    url(r'^index/', 'index.views.index'),
    ##其它个页面
    url(r'^hostinfo/', 'index.views.hostinfo'),
    url(r'^appinfo/', 'index.views.appinfo'),

    #############dns查询页面
    url(r'^dnsfind/', 'index.views.dnsfind'),
    url(r'^search/', 'index.views.search'),
    ##开发测试页面
    url(r'^devtest/', 'devtest.views.hostinfo'),
]

'''+ static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
        )
'''
