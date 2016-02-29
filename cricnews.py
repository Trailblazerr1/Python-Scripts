 #! /usr/bin/python3
from bs4 import BeautifulSoup
import requests

print ('Live Cricket news:')
print ('='*len('Live Cricket news:'))

url = "http://www.espncricinfo.com/rss/content/story/feeds/6.xml"
r = requests.get(url)
b = BeautifulSoup(r.text,"html.parser")
i=1
for d in b.find_all('item'):
    print(i,d.find('description').string)
    i+=1
