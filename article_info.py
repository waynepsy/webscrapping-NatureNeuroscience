import requests
from bs4 import BeautifulSoup as bs
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}

url = 'https://www.nature.com/articles/s41593-019-0496-y'
response = requests.get(url, headers=headers)
html=response.text
soup=bs(html,'lxml')
title = soup.find('div', id='content').h1.get_text()
print("Title: "+ title)
journal = soup.find('div', id='content').i.get_text()
print("Journal: "+ journal)
date = soup.find('div', id='content').a.get_text()
print("Date: "+ date)
name = soup.find('li',id='Aff1').ul.get_text()
print("Author: "+ name)
dep = soup.find('li',id='Aff1').h4.get_text()
print("Affiliation: "+ dep)












