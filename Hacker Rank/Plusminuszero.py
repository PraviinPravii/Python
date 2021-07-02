# -*- coding: utf-8 -*-
"""
Created on Fri May 14 19:29:16 2021

@author: Brain Hacker
"""
n=int(input())
lss=list(map(int,input().split()))
length=len(lss)
positive=0
negative=0
zero=0
def plusMinus(num,length):
    return num/length
    
    
for i in range(0,length):
    if lss[i]>0:
        positive+=1
    elif lss[i]<0:
        negative+=1
    else:
        zero+=1
print(plusMinus(positive, length))
print(plusMinus(negative, length))
print(plusMinus(zero, length))


