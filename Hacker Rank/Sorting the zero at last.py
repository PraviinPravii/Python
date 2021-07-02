# -*- coding: utf-8 -*-
"""
Created on Thu May 13 10:47:06 2021

@author: Brain Hacker
"""

x=[1,2,3,0,3,46,7,0]
y=""
z=[]
for i in range(0,len(x)):
    if x[i]==0:
        y+=str(x[i])
    else:
        z.append(x[i])
for j in range(len(y)):
    z.append(int(y[j]))
print(z)
    

        
    
        
        
        