import bs4 as bs
import urllib.request
import requests
import re
import json
import time
from requests.exceptions import RequestException
from multiprocessing.dummy import Pool
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import csv
from openpyxl import workbook

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
list1=[]
for num in range (1,5):
    urll = 'https://www.nature.com/search?order=relevance&journal=neuro&article_type=research&page='+ str(num)
    response = requests.get(urll, headers=headers)
    html=response.text
    soup=bs(html,'lxml')
    k = soup.find_all(href=re.compile("articles"))
    for t2 in k:
        t3 = t2.get('href')
        list1.append(t3)
    continue
url1=[]
title1=[]
journal1=[]
date1=[]
name1=[]
dep1=[]

for article_label in list1:
    url = 'https://www.nature.com'+ str(article_label)
    # print(url)
    response = requests.get(url, headers=headers)
    html=response.text
    soup=bs(html,'lxml')
    title = soup.find('div', id='content').h1.get_text()
    # print("Title: "+ title)
    journal = soup.find('div', id='content').i.get_text()
    # print("Journal: "+ journal)
    date = soup.find('div', id='content').a.get_text()
    # print("Date: "+ date)
    name = soup.find('li',id='Aff1').ul.get_text()
    # print("Author: "+ name)
    dep = soup.find('li',id='Aff1').h4.get_text()
    # print("Affiliation: "+ dep)
    url1.append(url)
    title1.append(title)
    journal1.append(journal)
    date1.append(date)
    name1.append(name)
    dep1.append(dep)

wb = workbook.Workbook()  # 创建Excel对象
ws = wb.active  # 获取当前正在操作的表对象
ws.append([u'url',u'title',u'journal',u'date',u'name',u'dep'])
for i in range(200):
    ws.append([url1[i],title1[i],journal1[i],date1[i],name1[i],dep1[i]])
    continue

wb.save('article.xlsx')
#
