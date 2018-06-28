#-*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
#取出number那一列的数据进行处理
data=pd.read_csv('E:/crawler weather.csv')
index=data['Number']
#print (index)
cValue = []
for i in range(len(index)):
    if index[i]<=50:
        cValue.append('limegreen')
    elif index[i]>100:
        cValue.append('orange')
    else:
        cValue.append('cornflowerblue')


plt.scatter(range(len(index)),index,color = cValue,marker = '*')
plt.title(u'杭州2017年6月空气质量指数')
a = []
for x in range(1,31):
    a.append(x)
plt.xticks(a,rotation = -30)#ratation顺时针旋转30
plt.xlabel(u'日期')
plt.ylabel(u'空气质量指数')
plt.show()