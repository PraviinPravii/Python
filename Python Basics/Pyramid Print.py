hassh=int(input())

liss=[]
for i in range(0,hassh+1):
    liss.append("#"*i)
for i in range(0,hassh+1):
    print(liss[i],end='\n')
print("\n")
for i in range(0,len(liss)):
    print(liss[-i],end='\n')

for i in range(-hassh,0):
    print(" "*abs(i)+liss[i],end='\n')
    
for i in range(0,len(liss)):
    print(" "*i+liss[-i],end='\n')
tmp=len(liss)
for i in range(0,hassh+1):
    if i==0:
        print("\n")
    else:
        print(" "*tmp+liss[i]+liss[i-1],end='\n')
    tmp=tmp-1
tmp=0
for i in range(0,len(liss)):
    if i==0:
        print("\n")
    else:
        print(" "*tmp+liss[-i]+liss[-i-1],end='\n')
    tmp=tmp+1

