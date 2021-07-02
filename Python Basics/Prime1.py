# -*- coding: utf-8 -*-
"""
Created on Fri May 21 07:39:34 2021

@author: Brain Hacker
"""

x=int(input())
for num in range(2,x):
    for i in range(2,num):
         if num%i==0: break
    else:
        print(num,"Prime")
   
