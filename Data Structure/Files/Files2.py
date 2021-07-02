# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:28:03 2020

@author: Hacker
"""

text=open("New Text Document.txt")
inp=text.read()
print("length of text file",len(inp))
print("string slicing",inp[0:10:1])
data=inp.find('r')
findsp=inp.find('o',data)
print("Data Find =o",inp[findsp])
strp=inp.strip()
print("with out space",strp)
print("r character memory location",data)
print(inp.upper())
print(inp.lower())
print(inp.isnumeric())
print(inp.isalnum())
print(inp.isalpha())
print(inp[4:9:],inp[4:7:].isalpha())
print(inp[39:44],inp[39:44:].isnumeric())
print(inp[0:3].isspace())