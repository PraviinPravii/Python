stuff=list()
while True:
    inp=input("Enter Number")
    if inp=="exit":
        break
    stuff.append(int(inp))
print("SUM:",sum(stuff))
print("Average",sum(stuff)/len(stuff))
print(stuff)

