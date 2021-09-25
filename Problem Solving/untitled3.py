# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 09:12:16 2021

@author: Brain Hacker
"""

def function(n):

   l2 = []

   for i in range(n):

       l = input()

       count = 0

       for i in l:

           if i == "#":

               count+=1

       l2.append(count)

   print(max(l2))

t = int(input())

for i in range (t):

    x = input().split()

n = int(x[0])

m = int(x[1])

function(n)