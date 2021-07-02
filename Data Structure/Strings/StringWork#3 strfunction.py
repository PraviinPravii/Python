upper=list()
lower=list()
stri="abcdefghijklmnopqrstuvwxyz"
def convert(a,b):
    up=""
    low=""
    for i in a:
        up+=i
    for j in b:
        low+=j
    print(up,low)

for i in range(0,len(stri)):
    a=stri[i]
    upper.append(a.upper())
    lower.append(a.lower())
print(upper)
print(lower)
convert(upper,lower)
    