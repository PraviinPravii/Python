def findmail(mail):
    if mail=="gmail":
        print("its a google mail")
    elif mail=="outlook":
        print("Its a microsoft mail")
    elif mail=="yahoo":
        print("Its a Yahoo mail")
while True:   
    usermail=str(input("Enter your Mail id:"))
    stri=""
    indexat=usermail.find("@")
    firstdotafterat=usermail.find(".",indexat)
    for i in range(indexat+1,firstdotafterat):
        stri+=usermail[i]
        string=usermail[indexat+1:firstdotafterat]
    findmail(stri.lower())
    findmail(string.lower())
    if usermail=="exit":
        break


