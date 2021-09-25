
Input =[12, 35, 9, 56, 24]
li=Input.copy()
li[0],li[4]=li[4],li[0]
print(li)


def swap(l):
    temp=l[0]
    l[0]=l[4]
    l[4]=temp
    print(l)
    
li=Input.copy()

swap(li)

get = li[-1], li[0]
li[0],li[4]=get[1],get[0]
print(li)

print(5/0)
li=Input.copy()
a=li[4],list(li[i] for i in range(1,4)),li[0]
for i in a:
    print(i,end="")






