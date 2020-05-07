import requests 
from bs4 import BeautifulSoup
from collections import Counter
from matplotlib import pyplot as plt

url = "https://www.cricbuzz.com/cricket-news/112912/the-cheatsheet"
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

all_text = soup.findAll("section",{"class":"cb-nws-dtlitms"})
list1 = []

for each_text in all_text:
    each_content = each_text.text
    words = each_text.text
    for word in words:
	list1.append(word)

count = {}

for word in list1:
    if word in count:
	count[word] += 1
    else:
	count[word] = 1

print("\n")

c = Counter(count)

top_word = c.most_common(5)
aa = dict(top_word)
print(aa)

value = list(aa.keys())
num = list(aa.values())


plt.xlabel("Top Five Words")
plt.ylabel("Occurance of the word")


plt.plot(value,num)
plt.show()    
