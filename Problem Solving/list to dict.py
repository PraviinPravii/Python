lis = ["Praveen", 3, "Acharya", 8, "Best", 10, "in ", 18, "Programming", 33]

liss=list()
dct=dict()
for i in range(0,len(lis),2):
    dct["Name"]=lis[i]
    dct["Number"]=lis[i+1]
    liss.append(dict(dct))
print(liss)
    

  
    
        
        
