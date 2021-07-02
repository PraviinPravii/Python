count=0
total=0
while True:
    inp=input("Enter a Number:")
    if inp=="exit":
        break  
    try:
        inpt=float(inp)
        count+=1
        total+=inpt
    except:
        print("Error, Entered Number is Invalid")
        continue
print("The sum of Numbers",total)
print("Count of Numbers",count)
print("Average of Number",total/count) 
