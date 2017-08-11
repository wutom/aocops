#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
python绘图核心模块,视图调用此模块可以生成需要的图形。
author：tom
date：201708
'''
##centos7 python2.7版本加载matplotib时需要特别的过程
import matplotlib
##设置图中字体的默认大小
matplotlib.rcParams.update({'font.size': 9})
matplotlib.rcParams['font.sans-serif'] = ['simhei']
matplotlib.use('Agg')
from matplotlib.pyplot import *
import matplotlib.pyplot as plt

'''
示例代码
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
#explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
##设置图形像素尺寸
plt.figure(figsize=(2,2))

#labeldistance 标签距离中心点
#pctdistance 比例数据距离中心

patches, l_text, p_text = plt.pie(sizes,labeldistance=1.2,pctdistance=0.7,labels=labels, autopct='%1.1f%%',shadow=False,startangle=90,radius=1.8,center=(0,1))
##图形是一个圆形
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#plt.legend() 侧边标签 默认关闭
plt.savefig("/tmp/test.png")
'''
#colors='yellowgreen', 'gold', 'lightcoral'，'lightskyblue'

###定义label函数返回列表
def matp_label(labels):
	lab = []
	for i in labels:
		lab.append(i)
	return (lab)

def matp_size(sizes):
	siz = ()
	siz = sizes
	return siz

def matp_figsize(figsize):
	figs = ()
	figs = figsize
	return figs


def matp_man(lab,siz,figs,path):
	plt.figure(figsize=figs)
	sizes = siz
	plt.pie(sizes,labeldistance=1.1,pctdistance=0.5,labels=lab, autopct='%1.1f%%',\
		shadow=False,startangle=90,)
	plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	#plt.legend()
	plt.savefig(path)
	plt.close()

if __name__ == '__main__':
	matp_man(lab,siz,figs,path)