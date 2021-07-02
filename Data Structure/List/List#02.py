strng="Hello Hi My Name is Praveen my Email is Praveena2253@gmail.com"
strrev=strng[::-1]
find=strrev.find("@")
fndspc=strrev.find(" ",find)
lst=strng.split("@")
length=lst[1]
email=""
for i in range(-fndspc,-find):
    email+=strng[i]
print(email+strng[-find::])