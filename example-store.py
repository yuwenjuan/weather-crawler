#-*- coding: utf-8 -*-
import csv, requests, re
from bs4 import BeautifulSoup
url = 'https://www.v2ex.com/?tab=all'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
articles = []
for div in soup.find_all(class_='cell item'):
    title = div.find(class_='item_title').get_text()
    category = div .find(class_='node').get_text()
    author = div .find(class_='topic_info').strong.string
    u = div .find(class_='item_title')
    link = 'https://www.v2ex.com' + re.findall(r'.*?href="(.+).*?"', str(u))[0]
    articles.append([title, category, author, link])
print (articles)
with open('E:/example-store.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['文章标题', '分类', '作者', '文章地址'])
    for row in articles:
        writer.writerow(row)
