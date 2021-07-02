inp=input("Enter Number")
temp=inp
try:
    inp=int(inp)
    print("Successfull")
except:
    inp=-1
if inp>=0:
    sum=1
    for i in range(1,inp):
        temp=inp
        sum*=temp
        inp-=1
    print("Factorial:",sum)
else:
    print("Error,Enter Correct Numbers")
        
    
    