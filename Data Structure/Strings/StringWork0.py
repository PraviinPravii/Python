lis=list()
def call(a):
    print(a)    
l="Praveen"
def convert(b):
    stri=""
    for i in b:
        stri+=i
    return stri       
for j in range(0,len(l)):
    for i in l:
        print(i)
    call(l[j])

while True:
    for i in range(0,len(l)):
        lis.append(l[i])
    print(lis)
    break       
print(convert(l))     