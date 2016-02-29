 #! /usr/bin/python3
from bs4 import BeautifulSoup
import requests
print('Movie/Tv series name:')
n = (input())
s=n.split()
m='+'.join(s)
#url= 'http://www.imdb.com/find?ref_=nv_sr_fn&q='+n'&s=all'
url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q='+m+'&s=all'

r = requests.get(url)
b = BeautifulSoup(r.text,"lxml")
for l in b.findAll('td',{'class':'result_text'}):
    href = l.find('a')['href']
    li = 'http://www.imdb.com'+href
    break

r2 = requests.get(li)
b2 = BeautifulSoup(r2.text,"lxml")

for div in b2.findAll('div',{'class':'ratingValue'}):
    print('Rating of '+n+ ' is',end='')
    print(div.text)
    print()

for s in b2.find_all('div',{'class':'summary_text'}):
    print('Summary of movie is :')
    print(s.text.lstrip())
    print()
