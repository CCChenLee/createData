#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt


x_input = list(range(1001))
y_input = [x**2 for x in x_input]
plt.scatter(x_input,y_input,c=y_input,cmap=plt.cm.Reds,edgecolor='none',s=30)
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
#设置刻度标记的大小
# plt.tick_params(axis='both',which='major',labelsize=14)
# plt.axis([0,1100,0,1100000])
plt.show()
plt.savefig('squares_plot.png',bbox_inches='tight')