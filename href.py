import requests
from bs4 import BeautifulSoup as bs
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
url = 'https://www.nature.com/search?order=relevance&journal=neuro&article_type=research'
response = requests.get(url, headers=headers)
html=response.text
soup=bs(html,'lxml')
# article_label = soup.find('div', {'id': 'content'}).find('a')
# print (article_label['href'])
for data in range(1,20):
    k = soup.find('h2', class_='h3 extra-tight-line-height').a
    article_label = k['href']
    print(article_label)




#
# # -*- coding:utf-8 -*-
# #python 2.7
# #XiaoDeng
# #http://tieba.baidu.com/p/2460150866
# #标签操作
#
#
# from bs4 import BeautifulSoup
# import urllib.request
# import re
#
#
# #如果是网址，可以用这个办法来读取网页
# #html_doc = "http://tieba.baidu.com/p/2460150866"
# #req = urllib.request.Request(html_doc)
# #webpage = urllib.request.urlopen(req)
# #html = webpage.read()
#
#
#
# html="""
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="xiaodeng"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# <a href="http://example.com/lacie" class="sister" id="xiaodeng">Lacie</a>
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html, 'html.parser')   #文档对象
#
#
# #查找a标签,只会查找出一个a标签
# #print(soup.a)#<a class="sister" href="http://example.com/elsie" id="xiaodeng"><!-- Elsie --></a>
#
# for k in soup.find_all('a'):
#     print(k)
#     print(k['class'])#查a标签的class属性
#     print(k['id'])#查a标签的id值
#     print(k['href'])#查a标签的href值
#     print(k.string)#查a标签的string
#     #tag.get('calss')，也可以达到这个效果
