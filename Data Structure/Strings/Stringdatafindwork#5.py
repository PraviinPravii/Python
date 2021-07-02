usermail=str(input("Enter your Mail id:"))
stri=""
indexat=usermail.find("@")
firstdotafterat=usermail.find(".",indexat)
print(indexat,firstdotafterat)
print(usermail[indexat],usermail[firstdotafterat])