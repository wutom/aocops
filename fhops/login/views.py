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
                response = HttpResponseRedirect('/index/')
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
