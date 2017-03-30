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

##加载user emial mobile数据库表
from login.models import user_ldap_mail_mobile
#import 自定义函数 
from api.ldap.bin import ldapauth, aliyunsms

###生成随机密码
def Makepass(length=8, chars=string.letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

##登陆表单类
class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    
###django 认证系统判定用户是否存在
def authDuser(username, password):
    user = authenticate(username=username,password=password)
    if user == username:
        return useradmin
    else:
        try:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.is_staff = True
            user.save()
            return user
        except User.DoesNotExist:
            user = User(username=username, password=password)
            user.set_password(password)
            user.is_staff = True
            user.save()
            return user
        return user
##登陆页面
def login(request):
    #server = request.META['HTTP_HOST']
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            
            ##调用ldap认证函数判断
            user = ldapauth.LDAPlogin(username,password)
            
            if user == 'True':
                ###对比djangoUser用户和重置已有用户密码
                authDuser(username,password)
                ##判断django自身auth系统账户，在后期登陆验证使用.
                user_auth = auth.authenticate(username=username, password=password)
                auth.login(request, user_auth)
                response = HttpResponseRedirect('/index/')
                response.set_cookie('username', username, 3600)
                return response
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login/login.html', {'uf':uf}, context_instance=RequestContext(request))

##重置密码表单类
class User_reset_Form(forms.Form):
    ##CHOICES = (('1', 'email',), ('2', 'ldap',))
    username = forms.CharField(max_length=24)
    mobile = forms.CharField(max_length=11)
    userid = forms.CharField(max_length=36)
    #废弃email_ldap = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES)

##重置密码函数
def reset_user_passwd(server,username,userid,mobile):
    ldap_user = user_ldap_mail_mobile.objects.filter(ldap=username, mobile=mobile)
    ##废弃email_user = user_ldap_mail_mobile.objects.filter(email=userid, mobile=mobile)
    mobile = str(mobile)
    mess1 = '重置密码异常:'
    mess2 = '新LDAP密码已发送到:' + mobile
    mess3 = 'LDAP用户名，邮箱地址或手机号码异常'
    mess4 = '发送短信异常'
    reset_response='''<p align=center>%s</p><p align=center><a href="http://%s/login/">返回登陆页</a></p>'''
    newpwd = Makepass()

    if ldap_user:
        resetpass = ldapauth.resetpass(username,newpwd)
        if resetpass == True:
            sms = aliyunsms.SmsSend(mobile,newpwd)
            if sms == 'True' and resetpass == True:
                return reset_response % (mess2, server)
            else:
                return reset_response % (mess4, server)
        else:
            return reset_response % (mess1, server)
    else:
        return reset_response % (mess3, server)

##重置密码表单页
def reset(request):
    server = request.META['HTTP_HOST']
    if request.method == 'POST':
        uf = User_reset_Form(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            userid = uf.cleaned_data['userid']
            mobile = uf.cleaned_data['mobile']
            message = reset_user_passwd(server,username,userid,mobile)
            return HttpResponse(message)
    else:
        uf = User_reset_Form()
    return render_to_response('login/resetuser.html', {'uf': uf}, context_instance=RequestContext(request))
            ##调用用户认证函数判断


##注销函数
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/") 
