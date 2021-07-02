a=int(input())
lss=[]
liss=[]
j=0
for i in range(a):
           lss=list(map(int,input().split()))
           liss.append(lss)


def primary_diagonal(a):
    j=0
    temp=0
    for i in range(0,a):
        temp+=liss[i][j]
        j+=1
    return temp


def secondarydiagonal(a):
    j=a-1
    temp=0
    for k in range(-a,0):
        temp+=liss[k][j]
        j-=1
    return temp
prime=0
secondary=0
prime=primary_diagonal(a)
secondary=secondarydiagonal(a)
a=prime-secondary
print(abs(a))

 
