#palindrome string
string = 'amama'
a=0
if len(string)%2!=0:
    a=int(len(string)/2)
    if string[0:]==string[::-1]:
        print("palindrome")
else:
    if string[:int(len(string)/2)]==string[int(len(string)/2):]:
        print("symmetrical")


# Function to reverse words of string 
string="Praveen Acharya"
a=string.split()
print(a[::-1])