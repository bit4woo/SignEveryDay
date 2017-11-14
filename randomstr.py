# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'

import hashlib
import random

x= "c0d5f885-fc12-4a6c-bd69-af4be5f1e4ee"

y="92971428acdfa920ba2f5649d0cb72a2"


def insert(insertto,index,string):
     return insertto[:index]+string+insertto[index:]
def insert_multi(z):
    for i in [8,12,16,20]:
        z = insert(z,i,"-")
    return z

print insert_multi(y)

def random_md5():
    i = 0
    result_list = []
    while i <= 10000:
        x =  random.randrange(1, 20000000000000000000000000000)
        md5 = hashlib.md5()
        md5.update(str(x))
        result_list.append( md5.hexdigest())
        i += 1
    return result_list

if __name__ =="__main__":
    result = []
    for item in random_md5():
        result.append(insert_multi(item))
    open("str.txt","w").writelines("\n".join(result))
