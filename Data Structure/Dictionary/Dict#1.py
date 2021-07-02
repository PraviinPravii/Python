dctry=dict()
while True:
    name=input("Enter Your Name:")
    if name=="exit":
        break
    Mob=input("Enter Your Mobile Number:")
    for i in range(0,4):
            dctry[name]=Mob
    
print(dctry)
