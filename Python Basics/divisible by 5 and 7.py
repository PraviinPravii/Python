# -*- coding: utf-8 -*-
"""
Created on Tue May 25 09:38:43 2021

@author: Brain Hacker
"""
liss=[12,24,35,70,88,120,155]
a=[]
for i in liss:
    if not(i%5!=0 and i%7!=0):
        a.append(i)   
for i in a:
    liss.remove(i)
print(liss)

