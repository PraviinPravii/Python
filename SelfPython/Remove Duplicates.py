# -*- coding: utf-8 -*-
"""
Created on Sun May 23 23:29:47 2021

@author: Brain Hacker
"""

#7.	Write a Python program to remove duplicates from a list
liss = [10,20,30,20,10,50,60,40,80,50,40]
dub_values=set()
b=[]
for i in liss:
    if i not in dub_values:
        b.append(i)
        dub_values.add(i)
print(b,dub_values)
    