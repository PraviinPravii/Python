inp=input("Enter something")

try:
    inp=int(inp)
    print("Its a Number")
except:
    print("its a string")