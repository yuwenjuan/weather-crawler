#-*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import re
mpl.rcParams['font.sans-serif'] = ['SimHei']

#data = pd.read_csv('E:/Jupter/web_crawl/weather.csv',encoding="gb2312")
data = pd.read_csv('E:/crawler weather.csv')
high_temp = data['TemperatureHigh']
#print high_temp
high_temp_new = []
for i in high_temp:
    high_temp_new.append(re.findall(r'\d+',i))
#print high_temp_new

low_temp = data['TemperatureLow']
low_temp_new = []
for j in low_temp:
    #print i
    low_temp_new.append(re.findall(r'\d+',j))
#print high_temp_new

date = range(1,31)

weather = data['Weather']
#print weather



plt.figure(figsize=(10, 6))
#plt.ylim(12,35)
plt.plot(range(len(weather)),high_temp_new,label=u'最高气温',linewidth=1,marker = 'o',linestyle = '--')
plt.plot(range(len(weather)),low_temp_new,label=u'最低气温',linewidth=1,marker = 'o',linestyle = '--')
plt.title(u'杭州2017年6月天气统计')
plt.legend(loc='best')
a = []
for x in range(1,31):
    a.append(x)
plt.xticks(a,rotation = -30)
plt.xlabel(u'日期')
plt.ylabel(u'温度')
plt.show()