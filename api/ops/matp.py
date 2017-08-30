#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
python绘图核心模块,视图调用此模块可以生成需要的图形。
author：tom
date：201708
'''
##centos7 python2.7版本加载matplotib时需要特别的过程
import matplotlib
import numpy as np
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
colors = ['gold','lightcoral','lightskyblue','blue','darkcyan','orange','yellowgreen']

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


def matp_pie(lab,siz,figs,path):
	plt.figure(figsize=figs)
	sizes = siz
	plt.pie(sizes,labeldistance=1.1,pctdistance=0.5,labels=lab, colors=colors, autopct='%1.1f%%',\
		shadow=False,startangle=90,)
	plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	#plt.legend()
	plt.savefig(path)
	plt.close()

'''
def drawBarChartPoseRatio(lab,lab_count,figs,path):  
    n_groups = 5      
    means_VotexF36 = (0.84472049689441, 0.972477064220183, 1.0, 0.9655172413793104, 0.970970970970971)    
    means_VotexF50 = (1.0,              0.992992992992993, 1.0, 0.9992348890589136, 0.9717125382262997)  
    means_VFH36    = (0.70853858784893, 0.569731081926204, 0.8902900378310215, 0.8638638638638638, 0.5803008248423096)  
    means_VFH50    = (0.90786948176583, 0.796122576610381, 0.8475120385232745, 0.8873762376237624, 0.5803008248423096)    
      
    fig, ax = plt.subplots()    
    index = np.arange(n_groups)    
    bar_width = 0.3    
    opacity   = 0.4    
      
    rects1 = plt.bar(index,             means_VFH36,    bar_width/2, alpha=opacity, color='r', label='VFH36'   )    
    rects2 = plt.bar(index+ bar_width/2,  means_VFH50,  bar_width/2, alpha=opacity, color='g', label='VFH50'   )    
     
    rects3 = plt.bar(index+bar_width, means_VotexF36,     bar_width/2, alpha=opacity, color='c', label='VotexF36')    
    rects4 = plt.bar(index+1.5*bar_width, means_VotexF50, bar_width/2, alpha=opacity, color='m', label='VotexF50')    
      
    plt.xlabel('Category') #    下标签
    plt.ylabel('Scores')    #   左标签
    plt.title('Scores by group and Category')    #标题
      
    #plt.xticks(index - 0.2+ 2*bar_width, ('balde', 'bunny', 'dragon', 'happy', 'pillow'))  
    plt.xticks(index - 0.2+ 2*bar_width, ('balde', 'bunny', 'dragon', 'happy', 'pillow')，fontsize =18)  
  
    plt.yticks(fontsize =18)  #change the num axis size  
  
    plt.ylim(0,1.5)  #The ceil  
    plt.legend()    
    plt.tight_layout()    
    plt.savefig(path)
	plt.close()  
'''

if __name__ == '__main__':
	matp_pie(lab,siz,figs,path)