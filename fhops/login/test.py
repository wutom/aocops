#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os,sys
def authlogin(username,password):
    if username == 'user' and password == '123456':
        return '1'
    else:
        return None

if __name__ == '__main__':
    authlogin(username,password)
