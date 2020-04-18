# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 07:19:11 2020

@author: shree
"""

fp=open('file4.txt','w')
import requests
from bs4 import BeautifulSoup

url="https://www.worldometers.info/coronavirus/"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
print(soup.prettify())


my_table=soup.find('table',{'id':'main_table_countries_today '})
table_row=soup.findAll('tr')


for i in table_row:
    table_data=soup.findAll('td')
    for j in table_data:
         if j.text=='':
             
             fp.write(" "+',')
         else:
             
             fp.write(j.text+',')
    fp.write('\n')
fp.write('\n')
    
    

