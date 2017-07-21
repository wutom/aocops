#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import MySQLdb
import json
reload(sys)
sys.setdefaultencoding('utf-8')
'''
   基础配置部分，定义文件和数据库信息
'''
####数据文件
hostfile = "../tempfile/host_info.json"
appfile = "../tempfile/app_info.json"

###数据库配置
dbcf={'dbhost':'localhost', 'dbuser': 'aoc', 'dbname': 'aoc', 'dbpwd': 'aoc'}

'''
   基础的文件信息格式化函数，待数据库更新函数调用
'''
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

'''
    数据库更新函数
    sql获取返回信息列表的唯一id server_id 或 app_id 然后对比数据库更新数据
'''
###更新host_info 文件信息
def hostinfoup(db_value):
    for v in db_value:
        machine_id = v[0]
        vm_cpu = v[1]
        hostname = v[2]
        vm_mem = v[4]
        lan_ipaddr = v[5]
        os_version = v[6]
        vm_types = v[8]
        vm_disk = v[9]
###基本SQL语句
        sqlinstert = "INSERT INTO vminfo_host_info(machine_id, vm_cpu, hostname, vm_mem, lan_ipaddr, os_version, vm_disk, vm_types) values ('%s','%s','%s','%s','%s','%s','%s','%s')" % (machine_id, vm_cpu, hostname.decode('unicode_escape'), vm_mem, lan_ipaddr, os_version, vm_disk, vm_types)

        sqlupdate = "UPDATE  vminfo_host_info SET vm_cpu='%s', hostname='%s', vm_mem='%s', lan_ipaddr='%s', os_version='%s', vm_disk='%s', vm_types='%s' WHERE machine_id='%s'" % (vm_cpu, hostname.decode('unicode_escape'), vm_mem, lan_ipaddr, os_version, vm_disk, vm_types, machine_id)

        cursor.execute("SELECT * FROM vminfo_host_info WHERE machine_id='%s'" % machine_id)
        results = cursor.fetchall()
###数据库操作
        if len(results) == 1:
            try:        ####判断数据库里面数据是否存在
                cursor.execute(sqlupdate)
                db.commit()
            except:
                db.rollback()
        else:
            try:
                cursor.execute("DELETE FROM vminfo_host_info WHERE machine_id='%s'" % machine_id)
                cursor.execute(sqlinstert)
                db.commit()
            except:
                db.rollback()


###更新 app_info 信息更新数据库
def appinfoup(db_value):
    for v in db_value:
        machine_id = v[0]
        app_name = v[1]
        app_listen = v[2]
        hostname = v[3]
        app_id = v[4]
        app_pid = v[5]
###基本SQL语句
        sqlinstert = "INSERT INTO vminfo_app_info(app_vm_id, hostname, app_listen, app_pid, app_name, app_id) values ('%s','%s','%s', '%s', '%s','%s')" % (machine_id, hostname, app_listen, app_pid, app_name, app_id)
        sqlupdate = "UPDATE  vminfo_app_info SET app_vm_id='%s', hostname='%s', app_listen='%s', app_pid='%s', app_name='%s' WHERE app_id='%s'" % (machine_id, hostname, app_listen, app_pid, app_name, app_id)

        cursor.execute("SELECT * FROM vminfo_app_info WHERE app_id='%s'" % app_id)
        results = cursor.fetchall()
###数据库操作
        if len(results) == 1:
            try:        ####判断数据库里面数据是否存在
                cursor.execute(sqlupdate)
                db.commit()
            except:
                db.rollback()
        else:
            try:
                cursor.execute("DELETE FROM vminfo_app_info WHERE app_id='%s'" % app_id)
                print sqlinstert
                cursor.execute(sqlinstert)
                db.commit()
            except:
                db.rollback()   

###主函数部分
if __name__ == '__main__':
    ##调用信息格式化函数
    host_value = filelist(hostfile)
    app_value = filelist(appfile)
    ##登陆数据库
    db = MySQLdb.connect('%s' % dbcf['dbhost'], '%s' % dbcf['dbuser'], '%s' % dbcf['dbname'], '%s' % dbcf['dbpwd'])
    cursor = db.cursor()

    ##调用数据库更新函数
    hostinfoup(host_value)
    appinfoup(app_value)

    ##关闭数据库
    cursor.close()
    db.close()
