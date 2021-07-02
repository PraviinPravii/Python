
"""If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird"""

n=int(input())
# if Loop is Needed
while True:
    if n%2!=0:
        print("Weird")
        break
    elif n%2==0 and (n>=0 and n<=5):
        print("Not weird")
        break
    elif n%2==0 and (n>=6 and n<=20):
        print("weird")
        break
    else:
        print("Not Weird")
        break
#with out loop
if n%2!=0:
    print("Weird")
elif n%2==0 and (n>=0 and n<=5):
    print("Not weird")
elif n%2==0 and (n>=6 and n<=20):
    print("weird")
else:
    print("Not Weird")
#Nested Loop
if n%2!=0:
    print("weird")
else:
    if n>=0 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird")
    else:
        print("Not Weird")