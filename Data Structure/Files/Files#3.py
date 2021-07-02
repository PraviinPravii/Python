fl=input("Enter File name")
try:
    fl=open(fl)
except:
    print("File Name is Error",fl)
    quit()

for i in fl:
    l=i.rstrip()
    if l.startswith("From"):
        continue
    print(l)