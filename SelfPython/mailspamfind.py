# -*- coding: utf-8 -*-
"""
Created on Sat May 22 10:33:15 2021

@author: Brain Hacker
"""

mail=str(input("Enter Your Mail Id:"))

at=mail.find('@')
spc=mail.find(".",at)
print(at,spc)
if '@' in mail:
    if mail.endswith('.com'):
        print("Its a correct Mail Address")
    else:
        print("This is spam mail addresss")
        
    