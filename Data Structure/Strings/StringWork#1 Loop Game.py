l="Hello"
j=1
for i in range(0,len(l)):
    print(l[0:i+1],l[-i-1:len(l)])
print("\n LOOP GAME \n")
for i in range(0,len(l)):
    print(l[i:len(l)],l[-i-1:])
    
    