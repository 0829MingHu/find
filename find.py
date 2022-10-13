import os
import shutil

num=0
apath=r"/home/chenj0g/rgb_flow/rgbflow"#1
bpath=r"/home/chenj0g/rgb_flow/move/rgb"#2

s=set()
flag=False
for curdir,roots,files in os.walk(apath):
    if flag==False:
        flag=True
        continue
    s.add(curdir.split('/')[-1])
m=set()
for i in s:
    print(apath+'/'+i)
    print(bpath+'/'+i)