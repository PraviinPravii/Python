# -*- coding: utf-8 -*-
"""
Created on Fri May 21 18:25:45 2021

@author: Brain Hacker
"""

x=int(input())
def prime(n):
    for i in range(2,n):
        if n%i==0:
            print(n,"Not Prime")
            break
    else:
        print(n,"Prime")
prime(x)

