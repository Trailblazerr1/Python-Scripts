 #! python3
from bs4 import BeautifulSoup
import requests
from twilio.rest import TwilioRestClient
import re

#start of function
def sends(body):
    ac_sid="XXXXXXXXXXXXXXXXXXXXXXXX"
    auth_token="XXXXXXXXXXXXXXXXXX"
    client=TwilioRestClient(ac_sid,auth_token)
    msg=client.messages.create(body=body,to="XXXXXXXXX",from_="XXXXXXXXX")
    print(msg.sid)
#end
while True:
    print ('Sending T-20 WC Live Cricket Scores:')
    url = "http://static.cricinfo.com/rss/livescores.xml"
    r = requests.get(url)
    b = BeautifulSoup(r.text,"html.parser")
    i=0
    j=1
    print('Wait.....')
    sc=[]
    for m in b.find_all(string=re.compile("951")):
        r = requests.get(m)
        b = BeautifulSoup(r.text,"html.parser")  
        for m in b.findAll('title'):
            i=i+1
            if i%2!=0:
                sc.append(m.text)
    sends(str(sc))
    print("%s sent"%(sc))
    break
