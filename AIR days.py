#-*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
data = pd.read_csv('E:/crawler weather.csv')
qua=data['Qai_lel']
qua2=qua.value_counts()
data=[]
for i in range(len(qua2)):
    data.append(qua2[i])
#print (data)
labels=qua2.index
plt.bar(range(len(qua2)),data,label=labels)
for a,b in zip(range(len(qua2)),data):
    plt.text(a,b+0.5,'%.0f'%b,ha='center',va='bottom',fontsize=11)
plt.title(u"空气质量天数统计")
plt.ylabel(u"天数")
plt.yticks(range(23),rotation = 30)
plt.xticks(rotation = 360)
plt.show()