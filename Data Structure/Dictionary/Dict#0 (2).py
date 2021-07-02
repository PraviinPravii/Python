sub=[]
marks=[]

for i in range(0,6):
    inps=input("Enter Subject:")
    inpm=input("Enter Marks of subject:")
    
    sub.append(inps)
    marks.append(inpm)

total=dict(zip(sub,marks))
print(total)
    