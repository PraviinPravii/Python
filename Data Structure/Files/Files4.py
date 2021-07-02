name=input("Enter File Name:")
try:
    text=open(name)
    count=0
except:
    print("Error, Enter Correct File name:",name)
for i in text:
    if i.startswith("From:"):
            i=i.rstrip()
            print(i)
            count+=1
            continue
            print(count)

