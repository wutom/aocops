#!/usr/bin/python
# -*- coding: utf-8 -*-
###

import ldap
#from pexpect import pxssh
import pxssh

host = "ldap://192.168.1.202"
bashDN = "ou=aijieli,dc=domain,dc=com"
Admin = "cn=Manager,dc=domain,dc=com"
Admin_pass = "password"
ssh_host = "192.168.1.202"
ssh_user = "root"
ssh_pass = "password"

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
			print "%s doesn't exist." %name
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
		child.prompt()
		child.logout()
		return True
	except Exception,e:
		return False
