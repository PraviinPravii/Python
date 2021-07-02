n=int(input("Enter range:"))
liss=[]
for i in range(n):
    lss=list(map(int,input().split()))
    liss.append(lss)

prime=0
temp=0
second=0
sum_list_row=list()
sum_list_column=list()

for i in range(0,len(liss)):
    prime+=liss[i][i]

liss.sort(reverse=True)


for i in range(0,len(liss)):
    second+=liss[i][i]

liss.sort(reverse=False)

for j in range(n):
    temp=0
    for i in range(n):
            temp+=liss[j][i]
    sum_list_row.append(temp)

for k in range(n):
    temp=0
    for i in range(n):
        temp+=liss[i][k]
    sum_list_column.append(temp)
    

print("sum of primary_diagonal:",prime)
print("sum of secondary_diagonal:",second)
for i in range(0,n):
    print("sum of",i+1,"row :",sum_list_row[i])
for i in range(n):
    print("sum of",i+1,"Column:",sum_list_column[i])
    
    
    
    
    
    
    