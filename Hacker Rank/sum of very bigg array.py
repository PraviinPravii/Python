# -*- coding: utf-8 -*-
"""
Created on Fri May 14 11:16:07 2021

@author: Brain Hacker
"""

def aVeryBigSum(ar,ar_count):
    sums=0
    for j in ar:
        for i in range(ar_count):
            sums+=ar[i]
        return sums
        


if __name__ == '__main__':

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))
 

    result = aVeryBigSum(ar,ar_count)
    print(result)
