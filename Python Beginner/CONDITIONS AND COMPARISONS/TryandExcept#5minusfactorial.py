inp=input("Enter Positive or Press Enter to do negative Factorial")
temp=inp
try:
    inp=int(inp)
    if inp>=0:
        print("Successfull")
        sum=1
        for i in range(1,inp):
            temp=inp
            sum*=temp
            inp-=1
        print("Factorial:",sum)
except:
    inp=int(input("Enter Nagative Number"))
    if inp<0:
        sum=-1
        for i in range(inp,0):
            temp=-inp
            sum*=temp
            inp+=1
        print(sum)