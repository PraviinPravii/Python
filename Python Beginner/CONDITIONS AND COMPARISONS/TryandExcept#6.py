def compute(a,b):
    total=a*b
    return total

days=input("Enter Days :")
rate=input("Enter rate :")
try:
    days=float(days)
    rate=float(rate)
    total=compute(days,rate)
    print("Pay",total)
    print("Pay",compute(days,rate))#short printing
except:
    print("Enter the numaric input")
    
inp=int(input("Enter Nagative Number"))
for i in range(inp,0):
    print(-(-i))
