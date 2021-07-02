# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:07:09 2021

@author: Brain Hacker
"""

#!/bin/python3



def simpleArraySum(lss,n):
    sss=0
    for i in range(0,n):
        sss+=lss[i]
    print(sss)
        
total=0
liss=[]
n=int(input())
inp=input().split()
for i in inp:
    liss.append(int(i))
simpleArraySum(liss,n)

