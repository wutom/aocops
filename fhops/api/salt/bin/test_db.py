#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import MySQLdb
import json
###数据文件
hostfile = "../tempfile/host_info.json"
appfile = "../tempfile/app_info.json"


###数据库基本配置
dbcf={'dbhost':'localhost', \
		'dbuser': 'aoc', \
		'dbname': 'aoc', \
		'dbpwd': 'aoc'}

###json数据格式化部分
def vallist(hostval):
    val = []
    for v in hostval:
        v = hostval[v]
        val.append(v)
    return (val)
### return 返回值只能是一个列表的形式
def filelist(fileval):
    hf = open(fileval)
    hostline = []
    for hfval in hf:
        fileval = json.loads(hfval)
        lineval = vallist(fileval)
        hostline.append(lineval)
    return hostline
    hf.close()


if __name__ == '__main__':
    ##调用主机信息格式化函数
    a = filelist(appfile)
    print a
