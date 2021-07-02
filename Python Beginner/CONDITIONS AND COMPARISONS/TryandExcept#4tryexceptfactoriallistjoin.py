inp=input("Enter something")

def attach(strng):
    
    for i in range(0,len(strng)):
        string=''
    print(string.join(strng))
    
def operation(inp):
    sum=1
    temp=int(inp)
    for i in range(1,inp):
        sum*=temp
        temp-=1
        
    print("Factorial:",sum)

def stringoperation(inp):
    strng=list()
    for i in range(0,len(inp)):
        strng.append(inp[i])
    print(strng)
    print(len(strng))
    attach(strng)
    
    
try:
    inp=int(inp)
    print("Its a Number")
    temp=inp
    operation(inp)
    
    
except:
    print("its a string")
    stringoperation(inp)
    

   
    

    


    
    
    