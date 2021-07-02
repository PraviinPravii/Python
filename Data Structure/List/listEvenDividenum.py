# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:00:07 2021

@author: Brain Hacker
"""

s=list(str(x) for x in range(1000,3000+1))
a=0
z=list()
for i in s:
    print(i if int(i[0])%2==0 and int(i[1])%2==0 and int(i[2])%2==0 and int(i[3])%2==0 else "".strip()) 
        