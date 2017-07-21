# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User, check_password
from django import forms
'''
#from .forms import Form
#自定义函数，项目同级目录
import ldapauth

class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
'''
###django 认证系统判定用户是否存在
def authenticate(username=None, password=None):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        # Create a new user. Note that we can set password
        # to anything, because it won't be checked; the password
        # from settings.py will.
        user = User(username=username, password=password)
        user.is_staff = True
        user.save()
        return 'True'
    return 'Flase'

print authenticate(username='wangtao', password='sdf89uy6')