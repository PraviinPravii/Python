sum=0
count=0
while True:
    inp=input("Enter number or type exit:")
    if inp=="exit":
        break
    else:
        sum+=int(inp)
        count+=1
        

print("Sum=",sum)
print("average=",sum/count)
