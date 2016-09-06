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
    f=open('Android.mk','a')
    f.write('LOCAL_PATH := $(call my-dir)\ninclude $(CLEAR_VARS)' + '\n')
    f.close()
    list_dirs = os.walk(rootDir) 
    for root, dirs, files in list_dirs: 
        for d in dirs: 
            print os.path.join(root, d)      
        for f in files: 
            if os.path.splitext(f)[1] == '.apk':
                str = os.path.basename(f) 
                #a = str.replace('.apk','')
                name,suffix = os.path.splitext(str)
                print name
                open('Android.mk','a').write(
            'LOCAL_MODULE :=' + name + '\n' +
            'LOCAL_MODULE_CLASS := APPS' + '\n' + 
            'LOCAL_MODULE_TAGS := optional' + '\n' + 
'LOCAL_BUILT_MODULE_STEM := package.apk' + '\n' + 
'LOCAL_MODULE_SUFFIX := $(COMMON_ANDROID_PACKAGE_SUFFIX)' + '\n'+
'LOCAL_SRC_FILES := $(LOCAL_MODULE).apk' + '\n' + 
'LOCAL_MULTILIB := 32' + '\n'+
'LOCAL_CERTIFICATE := PRESIGNED' + '\n'+
'include $(BUILD_PREBUILT)' + '\n'+
'\n'+
'\n'+
'\n')


#            lists = str.split('.')
#            print lists[0]

Iterate('.')
c = time.time() - start
print('程序运行耗时:%0.2f'%(c))
