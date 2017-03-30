#!/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb, os, sys
import urllib2, urllib
import json

###数据库配置
dbcf={'dbhost':'localhost', 'dbuser': 'aoc', 'dbname': 'aoc', 'dbpwd': 'aoc'}

##企业信息ID-KEY
corpid="0000ooooooooooooooooooooooo"
corpsecret="0000ooooooooooooooooooooooo"

##URL通过ID-KEY 获取token
corpurl_at = "https://api.exmail.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (corpid, corpsecret)
corpurl_user = "https://api.exmail.qq.com/cgi-bin/user/list?access_token=%s&department_id=1&fetch_child=1"

##URL修改邮箱密码
update_user_url = "https://api.exmail.qq.com/cgi-bin/user/update?access_token=%s"


###更新 app_info 信息更新数据库
def user_update(ldap,email,mobile):
###基本SQL语句
    sqlinstert = "INSERT INTO userlm(ldap, email, mobile) values ('%s','%s','%s')" % (ldap, email, mobile)
    cursor.execute("SELECT * FROM userlm WHERE mobile='%s'" % mobile)
    results = cursor.fetchall()

    if len(results) == 1:
    	return None
    else:
    	try:
    		cursor.execute("DELETE FROM userlm WHERE ldap='%s'" % ldap)
    		cursor.execute(sqlinstert)
    		db.commit()
    	except:
    		db.rollback()

#获取accesstoken
def accesstoken_req(url):
	atreq = urllib2.Request(url)
	atreq_data = urllib2.urlopen(atreq)
	at = json.loads(atreq_data.read())["access_token"]
	return at

#重置邮箱密码
def update_user_passwd(userid,passwd,user_up_url):
    atoken = accesstoken_req(corpurl_at)
    up_req = urllib2.Request(user_up_url % atoken, urllib2.urlencode({"userid": "test.wang@e-jiazi.com", "password": "password"}))
    return True

    
#获取用户邮箱地址和手机号码
def user_req(user_url):
	userreq = urllib2.Request(user_url)
	userlist = urllib2.urlopen(userreq)
	ul = json.loads(userlist.read())["userlist"]
	userlist = []
	for u in ul:
		###重新格式化邮箱前缀， tao.wang@xxxx.com --> wangtao
		ldap_data = u["userid"]
		ld = ldap_data.split('@')[0]
		if '.' in ld:
			ldap = str(ld.split('.')[1] + ld.split('.')[0])
			name = u["name"]
			email = str(u["userid"])
			mobile = str(u["mobile"])
			#print type(name), type(ldap), email, mobile
			user_update(ldap,email,mobile)


if __name__ == '__main__':
	##登陆数据库
    db = MySQLdb.connect('%s' % dbcf['dbhost'], '%s' % dbcf['dbuser'], '%s' % dbcf['dbname'], '%s' % dbcf['dbpwd'])
    cursor = db.cursor()

    ##调用数据库更新函数
    atoken = accesstoken_req(corpurl_at)
    user_url = corpurl_user % atoken
    user_req(user_url)
    ##关闭数据库
    cursor.close()
    db.close()


