# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User, check_password
from django import forms
from django.contrib import auth
from django.contrib.auth import authenticate
import sys, os, string, subprocess as sp
import commands
from random import choice

from api.ops import ldapauth

##登陆表单类
class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    
##登陆页面
def login(request):
    #server = request.META['HTTP_HOST']
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            ##判断django自身auth系统账户，在后期登陆验证使用.
            user_auth = auth.authenticate(username=username, password=password)
            if user_auth == None:
                return HttpResponseRedirect('/login/')
            else:
                auth.login(request, user_auth)
                response = HttpResponseRedirect('/')
                response.set_cookie('username', username, 3600)
                return response
        else:
            return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login/login.html', {'uf':uf}, context_instance=RequestContext(request))


##注销函数
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/") 


##重置密码表单类
class User_change_Form(forms.Form):
    ##CHOICES = (('1', 'email',), ('2', 'ldap',))
    username = forms.CharField(max_length=24)
    oldpwd = forms.CharField(widget=forms.PasswordInput())
    newpwd = forms.CharField(widget=forms.PasswordInput())
    newpwd_t = forms.CharField(widget=forms.PasswordInput())

##修改密码函数
def changpass(server,username,oldpwd,newpwd,newpwd_t):    
    mess1 = '新密码不一致'
    mess2 = '密码修改成功'
    mess3 = '密码修改失败'
    reset_response='''<p align=center>%s</p><p align=center><a href="http://%s/login/">返回登陆页</a></p>'''
    ##判断django自身auth系统账户，在后期登陆验证使用.
    if newpwd == newpwd_t:
        auth_ldap = ldapauth.changpass(username,oldpwd,newpwd)
        if auth_ldap == True:
            return reset_response % (mess2, server)
        else:
            return reset_response % (mess3, server)
    else:
        return reset_response % (mess1, server)
        
##修改密码页面
def cgp(request):
    server = request.META['HTTP_HOST']
    if request.method == 'POST':
        uf = User_change_Form(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            oldpwd = uf.cleaned_data['oldpwd']
            newpwd = uf.cleaned_data['newpwd']
            newpwd_t = uf.cleaned_data['newpwd_t']
            Changpass_Message = changpass(server,username,oldpwd,newpwd,newpwd_t)
            return HttpResponse(Changpass_Message)
    else:
        uf = UserForm()
    return render_to_response('login/changpass.html', {'uf':uf}, context_instance=RequestContext(request))

    