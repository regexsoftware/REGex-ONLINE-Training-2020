import matplotlib.pyplot as plt
import requests 
from bs4 import BeautifulSoup 
import operator 
from collections import Counter 
 
wordlist = [] 
source_code = requests.get("http://en.wikipedia.org/wiki/").text 

soup = BeautifulSoup(source_code, 'html.parser') 
 
for each_text in soup.findAll('p'): 
	content = each_text.text  

	words = content.lower().split() 
		
	for each_word in words: 
		wordlist.append(each_word) 
		  
clean_list =[] 
for word in wordlist: 
	symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
		
	for i in range (0, len(symbols)): 
		word = word.replace(symbols[i], '') 
			
	if len(word) > 0: 
		clean_list.append(word) 
 
word_count = {} 
	
for word in clean_list: 
	if word in word_count: 
		word_count[word] += 1
	else: 
		word_count[word] = 1()
				
c = Counter(word_count) 
	
top = c.most_common(5) 

print(top)

words, cnt = map(list, zip(*top)) 
  	
plt.bar(words,cnt)
plt.legend()
plt.xlabel("Words", fontsize=5)
plt.ylabel("Repeatations", fontsize=5)
plt.xticks(cnt, words, rotation=0)
plt.title("Top 5 repeated words")
plt.show()
