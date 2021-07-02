hassh=int(input())
strr=""
for i in range(hassh+1):
    print("#"*i," "*i)
print("\n")
for j in range(-hassh,0):
    print("#"*abs(j))
temp=hassh

for i in range(-temp,1):
    if hassh==abs(i):
        print("#"*abs(i))
        temp-=2
    else:
        print("#"+" "*abs(temp-1)+"#") 
        temp-=1
        if temp==0:
            print("#")
            break

temp1=hassh
for i in range(hassh):
    for l in range(0,temp1):
        print("#",end=' ')
    print("")

    temp1=temp1-1
    for j in range(0,i+1):
        print(end=' ')
        
print("\n")
temp2=hassh
for i in range(hassh):
    for l in range(0,temp2):
        print(end=' ') 
    temp2=temp2-1
    for j in range(0,i+1):
        print("#",end=' ')
    print("")
          
        




       
    
        
    
    
    
    
