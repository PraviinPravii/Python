
inp=input("Enter something")

try:
    inp=int(inp)
    print("Its a Number")
    if inp>=0:
        print("its a Positive Number")
    else:
        -print("ist a Negative Number")
except:
    print("its a string")

