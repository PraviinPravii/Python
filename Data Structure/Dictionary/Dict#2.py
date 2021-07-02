dct={}
dct["C"]=1
dct["&"]=7
dct["o"]=9
dct["55"]=75
lst=list()
for k,v in dct.items():
    lst.append((v,k))
lst=sorted(lst,reverse=True)
print(lst)

print(sorted([(k,v) for k,v in dct.items()]))