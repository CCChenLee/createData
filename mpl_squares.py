#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt

input_value = [1,2,3,4,5,6]
squares = [1,4,9,16,25,36]
plt.plot(input_value,squares,linewidth=5)
plt.title("Squares Numbers",fontsize=15)
plt.xlabel("Vaule",fontsize=15)
plt.ylabel("Square of Value",fontsize=15)
#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=15)
plt.show()