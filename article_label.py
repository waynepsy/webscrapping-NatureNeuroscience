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
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
urll = 'https://www.nature.com/search?order=relevance&journal=neuro&article_type=research'
response = requests.get(urll, headers=headers)
html=response.text
soup=bs(html,'lxml')
k = soup.find_all(href=re.compile("articles"))
for t2 in k:
    t3 = t2.get('href')
    print(t3)




