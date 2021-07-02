count=dict()
names=["as","an","44","as","an","as"]
print(type(count))
for i in names:
    count[i]=count.get(i,0)+1
    print(count)
