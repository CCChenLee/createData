#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
	rw = RandomWalk(50)
	rw.fill_walk()

	#设置绘图窗口的尺寸
	plt.figure(dpi=120,figsize=(10,6))

	point_numbers = list(range(rw.num_points))
	# plt.plot(rw.x_values,rw.y_values,
	# 	c=point_numbers,cmap=plt.cm.Blues,
	# 	edgecolor='none',s=1)
	# 	
	# plt.plot(0,0,c='blue',edgecolors='none',s=20)
	# plt.plot(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=30)
	
	plt.plot(rw.x_values,rw.y_values,color='#ff0000')
	# plt.plot(0,0,color='green')
	# plt.plot(rw.x_values[-1],rw.y_values[-1],color='red')

	# plt.axes().get_xaxis().set_visible(False)
	# plt.axes().get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Make another walk? (y/n):")
	#循环

# rw = RandomWalk()
# rw.fill_walk()
# plt.scatter(rw.x_values,rw.y_values,s=15)
# plt.show()

#调用random_walk.py提供的类