# -*- coding: utf-8 -*-
"""
Created on Sun May 23 23:38:52 2021

@author: Brain Hacker
"""

palindrome=input("Enter to checke Palindrome or Not:")
_str=list(i for i in palindrome.casefold())

_rev_str=list(x for x in _str[::-1])
print(_str,_rev_str)
s,rs="",""
for i in range(0,len(_str)):
    s+=_str[i]
for i in range(0,len(_rev_str)):
    rs+=_rev_str[i]
if s==rs:
    print("Palindrome")
else:
    print("Not Palindrome") 