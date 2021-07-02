# -*- coding: utf-8 -*-
"""
Created on Tue May 25 10:14:18 2021

@author: Brain Hacker
"""

a="H1e2l3l4o5w6o7r8l9d"
string=""
for i in a:
    if i.isalpha():
        b=a.index(i)
        if b%2==0:
            string+=i
print(string)

alpha="abcdefghijklmnopqrstuvwxyz"
a="H1e2l3l4o5w6o7r8l9d"
string=""
for i in a:
    if a.index(i)%2==0:
        if i in alpha.upper():
            string+=i
        if i in alpha.lower():
            string+=i
print(string)