fl=open('text.txt')
length=fl.read()
count=0
for i in range(0,len(length)):
    print(length[0:i])
for j in range(0,len(length)+1):
    print(length[-j:])