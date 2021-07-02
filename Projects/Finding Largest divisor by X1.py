num = int(input("Enter Number of elments:"))
temp=num
largest=0
check=0
number=list()
while temp>=1:
   numb= int(input("Enter Elements:"))
   number.append(numb)
   temp-=1

divisible=int(input("Enter Divisible X input"))
for i in range(0,len(number)):
            if number[i]%divisible==0:
                for j in range(1,len(number)):
                    if number[i]>number[j]:
                        largest=number[i]
                        check=1
                    else:
                        largest=number[j]
                        number[i]=number[j]
                        check=1
                
            else:
                break

if largest>=1:
        print("The Largest Number Divisable By X is",largest)
else:
        print("-1")
if check!=1:
    print("-1 Any number is not divisable by X")
