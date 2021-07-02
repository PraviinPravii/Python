# -*- coding: utf-8 -*-
"""
Created on Mon May 24 10:55:54 2021

@author: Brain Hacker
"""

string=input("Enter String:")
dicc=dict()
count=0
for i in string:
    dicc[i]=dicc.get(i,0)+1
print(dicc)
for i in dicc:
    print(i,dicc[i])
    


