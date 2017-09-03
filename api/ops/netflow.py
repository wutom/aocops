#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, sys, os
import datetime
import random
import MySQLdb
import time
reload(sys)
sys.setdefaultencoding('utf-8')


'''
创造数据生成json文件
ISOFORMAT='%Y-%m-%d %H:%M:%S'
now = datetime.datetime.now()

idc = 'ODC-1'
host_file = open("/tmp/flow.json", "w")
ty = 'in'

ft = {}
for i in range(0, 788400, 5):
	value = random.randint(60, 180)
	dl = now - datetime.timedelta(minutes=i)
	flow_time = dl.strftime(ISOFORMAT)
	ft['date'] = flow_time
	ft['idcname'] = idc
	ft['type'] = ty
	ft['value'] = value
	flow_load = json.dumps(ft)
	host_file.write(flow_load + '\n')

'''

host_file = "/tmp/odc-1-in-flow.json"
dbcf={'dbhost':'localhost', 'dbuser': 'aoc', 'dbname': 'aoc', 'dbpwd': 'aoc'}

def filelist(fileval):
	hf = open(fileval)
	for hfval in hf:
		fileval = json.loads(hfval)
		idcname = fileval['idcname']
		date_time = fileval['date']
		ty = fileval['type']
		val = fileval['vlaue']
		#print date_time, idcname, ty, val
		sqlinstert = "INSERT INTO idc_netflow(idc_name, date_time, flow_type, flow_value) values ('%s','%s','%s','%s')" % (idcname.decode('unicode_escape'), date_time, ty.decode('unicode_escape'), val)
		try:
			print sqlinstert
			cursor.execute(sqlinstert)
			db.commit()
		except:
			db.rollback()
	hf.close()

###主函数部分
if __name__ == '__main__':
	db = MySQLdb.connect('%s' % dbcf['dbhost'], '%s' % dbcf['dbuser'], '%s' % dbcf['dbname'], '%s' % dbcf['dbpwd'])
	cursor = db.cursor()

	##调用数据库更新函数
	filelist(host_file)

	##关闭数据库
	cursor.close()
	db.close()

