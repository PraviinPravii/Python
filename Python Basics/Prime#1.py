# -*- coding: utf-8 -*-
"""
Created on Fri May 21 20:52:00 2021

@author: Brain Hacker
"""

n=int(input())

data=[n%i!=0 for i in range(2,n)]

print(data)
print(type(data))
if all(data):
	print("prime")
else:
	print("not a prime")