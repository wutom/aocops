#!/usr/bin/python
# -*- coding: utf-8 -*-
###

import ldap
#####根据linux python版本加载 pxssh
from pexpect import pxssh
#import pxssh

###加载api的主配置文件获取必要的参数
from api.conf import config

host = config.LDAPCF['host']
bashDN = config.LDAPCF['bashDN']
Admin = config.LDAPCF['Admin']
Admin_pass = config.LDAPCF['Admin_pass']
##通过ssh到linux主机重置密码方式----暂不启用
ssh_host = config.LDAPCF['ssh_host']
ssh_user = config.LDAPCF['ssh_user']
ssh_pass = config.LDAPCF['ssh_pass']

def ldap_getcn(name):
	try:
		ldap.set_option(ldap.OPT_REFERRALS,0)
		conn = ldap.initialize(host)
		conn.protocol_version = ldap.VERSION3
		conn.simple_bind(Admin,Admin_pass)
 
		Filter = "(&(|(cn=" + name + ")))"       
		ldap_result_id = conn.search(bashDN,ldap.SCOPE_SUBTREE,Filter,None)

		result_data = conn.result(ldap_result_id,0)
		if result_data[1] == []:
			print "%s doesn't exist." % name
		else:
			LDID = result_data[1][0][0]
			return LDID
	except ldap.LDAPError, e:
		print e
		conn.unbind_s()

def LDAPlogin(username,password):
	try:
		ldap.set_option(ldap.OPT_REFERRALS,0)
		CN = ldap_getcn(username)
		login = ldap.initialize(host)
		login.simple_bind_s(CN,password)
		login.unbind_s()
		return 'True'
	except Exception,e:
		return 'Flase'

def changpass(username,oldpass,newpass):
	try:
		ldap.set_option(ldap.OPT_REFERRALS,0)
		CN = ldap_getcn(username)
		chang = ldap.initialize(host)
		chang.simple_bind_s(CN,oldpass)
		chang.passwd_s(CN,oldpass,newpass)
		return True
	except ldap.LDAPError,e:
		return False

def resetpass(username,newpwd="1234567"):
	try:
		ldap.set_option(ldap.OPT_REFERRALS,0)
		CN = ldap_getcn(username)
		shell_cmd = "ldappasswd -x -D " + Admin + " " + "-w " + Admin_pass + " " + CN + " " + "-s " + newpwd 
		child = pxssh.pxssh()
		child.login(ssh_host,ssh_user,ssh_pass)
		child.sendline(shell_cmd)
		child_status = child.prompt()
		if child_status == True:
			return True
		else:
			return False
		child.logout()
	except Exception,e:
		return False
