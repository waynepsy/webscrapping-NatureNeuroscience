import requests
from bs4 import BeautifulSoup as bs
import re
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
list1=[]
for num in range (1, 10):
    urll = 'https://www.nature.com/search?order=relevance&journal=neuro&article_type=research&page='+ str(num)
    response = requests.get(urll, headers=headers)
    html=response.text
    soup=bs(html,'lxml')
    k = soup.find_all(href=re.compile("articles"))
    for t2 in k:
        t3 = t2.get('href')
        list1.append(t3)
    continue


print(list1)