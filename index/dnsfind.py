#!/bin/env python
# -*- coding:utf-8 -*-

import os,sys
import dns.resolver

domain = sys.argv[1]
dnsip = sys.argv[2]


dns_find = dns.resolver.Resolver()
dns_find.nameserver=[dnsip]
anser = dns_find.query(domain)


dns = str(anser.response).split('\n')
ds = dns[8:]
dc = len(ds)
d = dict(zip(range(dc),ds))

for i in ds:
	print '<p>',i,'</p>'

'''
def re_dns_a(domain, dnstype, dnsip):
	dnsa = dns.resolver.Resolver()
	dnsa.nameserver=[dnsip]
	dnsa = dns.resolver.query(domain, dnstype)
	for i in dnsa.response.answer:
		for j in i.items:
			return j.address

def re_dns_c(domain, dnstype, dnsip):
	dnsc = dns.resolver.Resolver()
	dnsc.nameserver=[dnsip]
	dnsc = dns.resolver.query(domain, dnstype)
	for i in dnsc.response.answer:
		for j in i.items:
			return j.to_text()

def find_dns(domain, dnstype, dnsip):
	if dnstype == 'A':
		re_dns_a(domain, dnstype, dnsip)
	elif dnstype == 'CNAME':
		re_dns_c(domain, dnstype, dnsip)
	else:
		return 'error'

if __name__ == '__main__':
	find_dns(domain, dnstype, dnsip)

'''