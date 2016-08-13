import requests
import json

req = requests.get('http://api.open-notify.org/astros.json')
list = []
p=json.loads(req.text)

list.append(p)
userData = {}
parsedData= []

for data in list:
    userData['message'] = data['message']
    userData['number'] = data['number']
    #userData['people'] = data['people']

print('No of people in space :')
print(userData['number'])
    
parsedData.append(userData)    
    #return render(request, 'people/index.html', {'data': parsedData})