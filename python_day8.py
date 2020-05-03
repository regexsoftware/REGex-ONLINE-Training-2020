# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:26:25 2020

@author: shree
"""


import requests
from bs4 import BeautifulSoup
from collections import Counter 
from matplotlib import pyplot as plt
url="https://www.cricbuzz.com/cricket-news/112912/the-cheatsheet"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')

all_text=soup.findAll("section",{"class":"cb-nws-dtl-itms"})
list1=[]
for each_text in all_text:
    each_content=each_text.text
    words=each_content.split()
    for word in words:
     list1.append(word)
#print(list1)
count={}

for word in list1:
    if word in count:
       count[word]+=1
    else: 
       count[word] = 1
print("\n")

c = Counter(count) 
top_word = c.most_common(5) 
aa=dict(top_word)
print(aa)
value=list(aa.keys())
num=list(aa.values())
plt.xlabel("Top five words")
plt.ylabel("Occurance of the word")
plt.plot(value,num)
plt.show()

#%%
#ques-2
from textblob import TextBlob
import speech_recognition as sr
r=sr.Recognizer()
my_mic=sr.Microphone(device_index=1)
with my_mic as source:
    print("Say..!!")
    audio=r.listen(source)
data=r.recognize_google(audio)
print(data)
 
 
def sentiment(polarity):
    if blob.sentiment.polarity < 0:
        print("Negative")
    elif blob.sentiment.polarity > 0:
        print("Positive")
    else:
        print("Neutral")
 
 
blob = TextBlob(data)
print(blob.sentiment)
sentiment(blob.sentiment.polarity)
 
#%%
#ques-3


import folium 
from matplotlib import pyplot as plt
from geopy.geocoders import Nominatim
import pandas as pd
df=pd.read_csv('farm_data.csv')

#----PIE CHART----
list2=[]
list3=[]

list1=list(df["Location"])

for i in list1:
    li=i.split(',')
    list2.append(li)

for i in list2:
    if i[1] not in list3:
        list3.append(i[1])

count={}
for word in list2:
    if word[1] in count:
        count[word[1]]+=1
    else: 
        count[word[1]] = 1
    
print("\n")
farm=df["Farm_Name"]

percent=count.values()
location=count.keys()
print(count)
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b","#7c564b","#2c564b"]
explode=(0.1,0,0,0,0,0)
plt.pie(percent,labels=location,colors=colors,explode=explode,autopct='%1.1f%%', shadow=True, startangle=140)
plt.show()

#------------MAP------------
geolocator = Nominatim()

Farm = df["Farm_Name"]
Farm_list = list(Farm)
state = df["Location"]
state_list = list(state)

address = [Farm_list[i] + " " + state_list[i] for i in range(0, len(Farm_list))] 

mapit = folium.Map( location=[20.5937, 78.9629], zoom_start=6 )

for i in  address:
	loc = geolocator.geocode(i)
	lat = loc.latitude 
	long = loc.longitude
	folium.Marker( location=[ lat, long ], fill_color='#43d9de', radius=8 ).add_to( mapit )
mapit.save( 'Farm_map.html')

