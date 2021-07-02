# -*- coding: utf-8 -*-
"""
Created on Wed May 19 08:17:18 2021

@author: Brain Hacker
"""
#Arm strong 

n=int(input())
lenght=len(str(n))
temp=n
summ=0
while temp>0:
    summ+=(temp%10)**lenght
    temp//=10 
if summ==n:
    print("Arm Strong")
else:
    print("Not arm strong")
    
    

   