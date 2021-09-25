# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 21:25:34 2021

@author: Brain Hacker
"""

def solve (N, ch):
    # Write your code here
    st=str()
    for i in range(N):
        st+=ch[i]
    return st
        

N = 5
ch = "H e l l o".split()

out_ = solve(N, ch)
print (out_)