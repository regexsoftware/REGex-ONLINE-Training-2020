# Question -  7
"""
7. #### MAIN TASK ####
    - To scrap data from worldometer example: INDIA Data and run it
        on live mode.
    - Print Additionally total number of Coronavirus
        Cases, Deaths, Recovered.
"""

#Solution:

import requests #handles the http requests
from bs4 import BeautifulSoup # used to parse html data

url = "https://www.worldometers.info/coronavirus/"
page = requests.get(url) # generating http request
print(page) # response 200 means OK

page = page.text  # to get the html code text
print(page)

soup = BeautifulSoup(page, "html.parser") # two parameters(#data, #parse)
print(soup) #here the parsed html code is stored

# find(div/section/head/body/h1/etc >> Tags, {class/id/xpath  >> Attr : "attr_name" })
a = soup.find("div", {"class" : "maincounter-number"})
print(a)
print(a.text) # for only printing the text inside a


# printing all the text in h1 tags
b = soup.find_all("h1")
for i in b:
    print(i.text)
    
# for getting all three datas
c = soup.find_all("div", {"class" : "maincounter-number"})
for i in c:
    print(i.text)
    
    
