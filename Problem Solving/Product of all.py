n=int(input())
l=input().split()
s=1
for i in l:
    s=(s*int(i))%(10**9+7)
print(s)
    