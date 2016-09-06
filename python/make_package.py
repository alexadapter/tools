# -*- coding:utf-8 -*-
import re
import os
import time
#str.split(string)分割字符串
#'连接符'.join(list) 将列表组成字符串
start = time.time()

#for i in range(0,1000):f.write(str(i)+'\n')
#f.close()
def Iterate(rootDir): 
    list_dirs = os.walk(rootDir) 
    for root, dirs, files in list_dirs: 
        for d in dirs: 
            print os.path.join(root, d)      
        for f in files: 
            if os.path.splitext(f)[1] == '.apk':
                str = os.path.basename(f) 
                #a = str.replace('.apk','')
                name,suffix = os.path.splitext(str)
                name+=" \\"
                print name
                #            lists = str.split('.')
#            print lists[0]

Iterate('.')
c = time.time() - start
print('程序运行耗时:%0.2f'%(c))
