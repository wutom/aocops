#!/usr/bin/python
# -*- coding: utf-8 -*-
import salt.client as sc
import json,redis
import aliyun_grains
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
    1.load_grains 获取所有主机的grains值
    2.写入到host_info.json和app_info.json
    3.从redis获取阿里云信息写入到host_info.json
'''
######################redis信息
rs = redis.Redis(host='redis.210', port=7100, db=0)
aliyun_host_info = json.loads(rs.get('aliyun_host_info'))
host_count = aliyun_host_info['TotalCount']
host_values = aliyun_host_info['Instances']
host_value = host_values['Instance']
############################################################
###salt调用
local = sc.LocalClient()
hostonline = local.cmd('*', 'test.ping', timeout=5)
###刷新grains信息
reloadhost = local.cmd('*', 'saltutil.sync_grains', timeout=5)
###目标主机指定
def host_info():
    try:
        host_file = open("../tempfile/host_info.json", "w")
        gra = {}
        for hl in hostonline:
            grains = local.cmd(hl, "grains.items")
            for i in grains.keys():
                ip4 = grains[i]["ipv4"]
                ip4 = list(ip4)
                ip4.remove('127.0.0.1')
                gra['ipv4'] = ip4[0]
                gra['hostname'] = grains[i]["fqdn"]
                gra['server_id'] = grains[i]["server_id"]
                gra['os'] = grains[i]["osfinger"]
                gra['types'] = grains[i]["virtual"]
                gra['cpu_types'] = grains[i]["cpu_model"]
                gra['cpu_num'] = grains[i]["num_cpus"]
                gra['mem'] = grains[i]["mem_total"]
                gra['disk_root'] = grains[i]["disk_root_total"]
                gra['disk_opt'] = grains[i]["disk_opt_total"]
            gra_load = json.dumps(gra)
            host_file.write(gra_load + '\n')
    except Exception,e:
        print "Exception:\n",e
    finally:
        host_file.close()

###aliyun add
def aly_host_info():
    try:
        host_file = open("../tempfile/host_info.json", "a+")
        gra = {}
        for hl in range(host_count):
            gra['ipv4'] = host_value[hl]["PublicIpAddress"]["IpAddress"][0]
            gra['hostname'] = host_value[hl]["InstanceName"]
            gra['server_id'] = host_value[hl]["InstanceId"]
            gra['os'] = "CentOS6"
            gra['types'] = host_value[hl]["InstanceType"]
            gra['cpu_types'] = host_value[hl]["InstanceType"]
            gra['cpu_num'] = host_value[hl]["Cpu"]
            gra['mem'] = host_value[hl]["Memory"]
            gra['disk_root'] = "40"
            gra['disk_opt'] = "300"
            gra_load = json.dumps(gra)
            host_file.write(gra_load + '\n')
    except Exception,e:
        print "Exception:\n",e
    finally:
        host_file.close()


def app_info():
    try:
        app_file = open("../tempfile/app_info.json", "w")
        gra = {}
        for hl in hostonline:
            grains = local.cmd(hl, "grains.items")
            for i in grains.keys():
                app_num = grains[i]["app_num"]
                int(app_num)
                appinfo = {}
                for app in range(app_num):
                    app = app + 1
                    num = 'app' + str(app)
                    appinfo = grains[i][num]
                    gra['hostname'] = grains[i]["fqdn"]
                    sid = gra['server_id'] = grains[i]["server_id"]
                    aid = gra['app_pid'] = appinfo['app_pid']
                    gra['app_name'] = appinfo['app_name']
                    gra['app_listen'] = appinfo['app_listen']
                    gra['app_id'] = str(sid) + str(aid)
                    gra_load = json.dumps(gra)
                    app_file.write(gra_load + '\n')
    except Exception,e:
        print "Exception:\n",e
    finally:
        app_file.close()

if __name__ == '__main__':
    host_info()
    app_info()
    aly_host_info()