import os
import io
import requests
from PIL import Image

print('Enter no of photos:')
no = input()
no = int(no)
no=no+1
print('-----------------Started------------------')
for m in range(1,no):
    out_dir="C:\\Users\\Anurag\\Desktop\\wallp"
    url="http://img.infinitynewtab.com/wallpaper/"
    furl = url + str(m) +".jpg" 
    p=list(furl)
    q=''.join(p)
    r = requests.get(q, stream=True,verify=False)
    
    
    if r.status_code == 200:
        i = Image.open(io.BytesIO(r.content))
        i.save(os.path.join(out_dir, str(m))+'.jpg', quality=50)
        print(m)
        
        
    else:
        print('U r out of luck! Check ur internet')
print('Done :P')

