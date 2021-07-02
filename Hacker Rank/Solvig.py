x, y, z, n = (int(input()) for _ in range(4))
r=[]
a=[]

for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
                r.append([i,j,k])

for m in r:
    if sum(m)!=n:
        a.append(m)
print(a)
