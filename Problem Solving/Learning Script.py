# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 13:33:02 2021

@author: Learning Script
"""

t=int(input())


for i in range(t):
    n=int(input())
    li=[]
    for i in range(n):
        li.append(list(map(int,input().split())))
    cnt=0
    for m in range(n):
        for j in range(n):
            for i in range(m,n):
                for k in range(j,n):
                    if li[m][j]>li[i][k]:
                        cnt+=1
                
    print(cnt)

