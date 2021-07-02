def compareTriplets(a, b):
    if a>b:
        return True
    elif a<b:
        return False

    

if __name__ == '__main__':
    

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))
c=0
d=0
for i in range(0,len(a)):
    result=compareTriplets(a[i],b[i])
    if result==True:
        c+=1
    elif result==False:
        d+=1
print(c,d)
        



