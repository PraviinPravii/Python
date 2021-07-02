# -*- coding: utf-8 -*-
"""
Created on Thu May 20 20:25:59 2021

@author: Brain Hacker
"""

n=int(input())
liss=list(i for i in range(0,n))
liss.clear()
lss_name=list()
lss_grade=list()
for i in range(0,n):
    name,grade=list(map(str, input().split())),list(map(float, input().split()))
    lss_name.append(name)
    lss_grade.append(grade)
    for i in range(0,len(lss_name)):
        liss.append(lss_name+lss_grade)
        lss_grade.clear()
        lss_name.clear()
print(liss)

        