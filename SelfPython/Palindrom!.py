# -*- coding: utf-8 -*-
"""
Created on Sun May 23 22:01:45 2021

@author: Brain Hacker
"""


my_str = 'aIbohPhoBiA'
my_str = my_str.casefold()
rev_str = my_str[::-1]
if my_str == rev_str:
   print("It is palindrome")
else:
   print("It is not palindrome")

