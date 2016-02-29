import os,shutil
l=os.listdir()
for file in l:
        if file.lower().endswith('.mp4') or file.endswith('.mkv') or file.endswith('.avi'):
                os.makedirs('Vid',exist_ok=True)
                shutil.move(r"./"+file,'./Vid')
        if file.lower().endswith('.jpeg') or file.endswith('.png') or file.endswith('.jpg'):
                os.makedirs('Photos',exist_ok=True)
                shutil.move(r"./"+file,'./Photos')    
        if file.lower().endswith('.mp3') or file.endswith('.ogg') or file.endswith('.wav'):
                os.makedirs('Songs',exist_ok=True)
                shutil.move(r"./"+file,'./Songs')    