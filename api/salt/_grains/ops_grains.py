#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
import statvfs
from datetime import datetime

##OPS 自定义grains 项目

## DISK DIR= '/', '/opt'
def disk_info():
    disk_dir = {'disk_root':'/', 'disk_opt':'/opt'}
    disk_size = {}
    for name in disk_dir:
        vfs_dir = disk_dir[name]
        vfs = os.statvfs(vfs_dir)
        disk_total = vfs[statvfs.F_BLOCKS]*vfs[statvfs.F_BSIZE]/(1024*1024*1024)
        disk_free = vfs[statvfs.F_BFREE]*vfs[statvfs.F_BSIZE]/(1024*1024*1024)
        disk_size[name + '_total'] = disk_total
        disk_size[name + '_free'] = disk_free
    return disk_size

def app_info(appid):
    appinfo = {}
    appname = appid[6].split('/')[1]
    apppid = appid[6].split('/')[0]
    applisten = appid[3]
    appinfo['app_name'] = appname
    appinfo['app_pid'] = apppid
    appinfo['app_listen'] = applisten
    return appinfo

def app_list():
    appfind = os.popen('netstat -nltp').readlines()
    appok = appfind[2:]
    applist = {} 
    num = 0
    for appid in appok:
        num += 1
        appid = appid.split()
        app = app_info(appid)
        applist['app' + str(num)] = app
    applist['app_num'] = num
    return applist

'''
调试函数输出,更新到/srv/salt/_grains/ 请注销掉
'''
print disk_info()
print app_list()
