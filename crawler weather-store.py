#-*- coding: utf-8 -*-
import importlib
import sys,csv
importlib.reload(sys)#编码转换
import pandas as pd
from pandas import DataFrame,Series

from bs4 import BeautifulSoup
import requests
def data_parser(tr_temp):
    info=[]
    for string in tr_temp.stripped_strings:
        info.append(string)
    return info
def collect_data(url_temp,database_temp):
    #获取整个网页信息——非结构化数据
    res = requests.get(url_temp)
    res.encoding='utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    #找到一个月天气变化的表单
    weather_grid=soup.find_all('div',{'class':'data-table'})
    weather=weather_grid[0].find_all('tr')
    for tr in weather:
        database_temp.append(data_parser(tr))
    database_temp.pop(0)#删除第一个元素
    return database_temp

def main():
    url='http://tianqi.eastday.com/hangzhou_history/58457_201706.html?btype=historyWeather&subtype=pre&idx=1'
    database=[]
    page=collect_data(url,database)#page为[[],[],[]]格式
    with open('E:/crawler weather-store.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Date','Week','TemperatureLow','TemperatureHigh','Weather','Wind','Number','Qai_lel'])
        for row in page:
            writer.writerow(row)
if __name__ == '__main__':
    main()