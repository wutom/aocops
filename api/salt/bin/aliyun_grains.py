#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, redis

rs = redis.Redis(host='redis.210', port=7100, db=0)

aliyun_host_info = json.loads(rs.get('aliyun_host_info'))

host_count = aliyun_host_info['TotalCount']
host_values = aliyun_host_info['Instances']
host_value = host_values['Instance']


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
 
if __name__ == '__main__':
	aly_host_info()