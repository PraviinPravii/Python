# -*- coding: utf-8 -*-
"""
Created on Fri May 14 06:46:48 2021

@author: Brain Hacker
"""

n=int(input())
j=list(map(int, input().split(" "))) 
print(type(j[1]))
a=list(j)
mx=[]
a=set(a)
a=list(a)
temp=0
lent=len(a)

for i in range(0,lent):
    mx.append(max(a))
    temp=max(a)
    a.remove(temp)
print(mx[1])
    
  
    

    

        
        
    



        
        
    

    
    
    
    


