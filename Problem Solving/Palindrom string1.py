"""st="aba"

if len(st)%2==0:
    a=st[:int(len(st)/2)]
    b=st[int(len(st)/2):]
    print(a,b)
    if a==b[::-1]:
        print("YES")
    else:
        print("NO")

else:
    a=int(len(st)/2+0.5)
    b=st[a::]
    c=st[::-a]
    if c[::-1]==b:
        print("YES")
    else:
        print("NO")
    
"""
def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "aba"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")