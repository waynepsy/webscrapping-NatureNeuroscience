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
import unicodedata
import xlwt
from xlwt import Workbook
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
list1=[]
for num in range (1,11):
    urll = 'https://www.nature.com/search?order=relevance&journal=neuro&article_type=research&page='+ str(num)
    response = requests.get(urll, headers=headers)
    html=response.text
    soup=bs(html,'lxml')
    k = soup.find_all(href=re.compile("articles"))
    for t2 in k:
        t3 = t2.get('href')
        list1.append(t3)
    continue
title1=[]
journal1 = []
date1 = []
name1 = []
dep1 = []
body = []
url1 = []
a_list1=[]
urlist=[]
for article_label in list1:
    url = 'https://www.nature.com'+ str(article_label)
    # print(url)
    response = requests.get(url, headers=headers)
    html=response.text
    soup=bs(html,'lxml')
    urlist=['https://www.nature.com'+ str(article_label)]

    title = [soup.find('div', id='content').h1.get_text()]
    journal = [soup.find('div', id='content').i.get_text()]
    date = [soup.find('div', id='content').a.get_text()]
    a_list = [a.get_text('|', strip=True) for a in soup.find_all('ul', class_='pa0 inline-list text14 standard-space-below')]
    if soup.find('h3', class_='emphasis') is not None:
        dep_list = [h3.get_text() for h3 in soup.find_all('h3', class_='emphasis')]
    else:
        dep_list = 0
    # if soup.find('ul', class_='c-article-author-affiliation__authors-list') is not None:
    #     name_list = [ul.get_text() for ul in soup.find_all('ul', class_='c-article-author-affiliation__authors-list')]
    # else:
    #     name_list = 0
    a_list1.append(a_list)
    url1.append(urlist)
    title1.append(title)
    journal1.append(journal)
    date1.append(date)
    # name1.append(name_list)
    dep1.append(dep_list)
    # print(url1)
    # print(title1)
    # print(journal1)
    # print(date1)
    # # print(name1)
    # print(dep1)
    # print(a_list1)

#
# wb = workbook.Workbook()  # 创建Excel对象
# ws = wb.active  # 获取当前正在操作的表对象
# ws.append([u'url',u'title',u'journal',u'date',u'dep',u'a_list1'])
# for i in range(50):
#     ws.append([url1[i],title1[i],journal1[i],date1[i],dep1[i],a_list1[i]])
#     continue
#
# wb.save('article.xlsx')
# #
header = ['url', 'title', 'journal', 'date', 'keywords', 'dep']
with open('output.csv', 'w',newline='',encoding="utf-8") as f:
    f_csv = csv.writer(f)
    f_csv.writerow(header)
    f_csv.writerows(zip(url1, title1, journal1, date1, a_list1, dep1))
