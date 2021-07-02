list =["Hi","Hello","How","are","you"]

for li in list:
    print("list",li)
for i in range(len(list)):
    list[i]=list[i].upper()
    print(list[i])
    list[i]=list[i].lower()
    print(list[i])
    list[i]=list[i].capitalize()
    print(list[i])
    