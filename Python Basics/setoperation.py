# -*- coding: utf-8 -*-
#using set function
liss1=[1,3,6,78,35,55]
liss2=[12,24,35,24,88,120,155]
print(set(liss1).intersection(set(liss2)))
print(set(liss2).intersection(set(liss1)))
print(set(liss1).difference(set(liss2)))
print(set(liss2).difference(set(liss1)))

#using Operators
print(set(liss1)^(set(liss2)))
print(set(liss2)^(set(liss1)))
print(set(liss1)&(set(liss2)))
print(set(liss2)&(set(liss1)))
print(set(liss1)-(set(liss2)))
print(set(liss2)-(set(liss1)))
print(set(liss1)|(set(liss2)))
print(set(liss2)|(set(liss1)))

#using loops an condition
a=dir(set(liss1))
for j in a:
    if j=="intersection":
        for i in liss1:
            if i in liss2:
                print(i)
        for i in liss2:
            if i in liss1:
                print(i)
    if j=="difference":
        for i in liss1:
            if i not in liss2:
                print(i,end=',')
        print("\n")
        for i in liss2:
                if i not in liss1:
                    print(i,end=',') 
        print("\n")

        for i in liss1:
            if i not in liss2:
                print(i,end=',')
        for i in liss2:
            if i not in liss1:
                print(i,end=",")
        print("\n")   
        for i in liss2:
            if i not in liss1:
                print(i,end=',')
        for i in liss1:
            if i not in liss2:
                print(i,end=",")            
    

