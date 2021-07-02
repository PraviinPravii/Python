inp=input("Enter something")
def checkintstr(a):
    try:
        a=int(a)
        print("Its a Number")
    except:
        print("Its a string")


checkintstr(inp)