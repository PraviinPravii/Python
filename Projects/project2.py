#using rollnumber control
priyanka=1
shruti=2
ramya=3
kavitha=4
praveen=5
print("Teacher calling name Please say your roll number \n ")

print("If Present Say Your Roll number otherwise if absent give Enter \n")
present=0
absent=0
print("Priyanka")
a=input("Enter Your Roll Number:")
try:
    a=int(a)
except:
    a="priyanka"
    print(a,"Not Answered or Not answered correctly considered as Absent \n")
    absent+=1 
    
if a==priyanka:
    print("Roll No",priyanka) 
    a="priyanka"
    print(a," is Present \n")
    present+=1
    
elif a!=priyanka:
    a="priyanka"
    print(a,"This is not your Roll Number considered as absent \n")
    absent+=1 

print("shruti")
a=input("Enter Your Roll Number:")
try:
    a=int(a)
except:
    a="shruti"
    print(a,"Not Answered or Not answered correctly considered as Absent \n")
    absent+=1 
    
if a==shruti:
    print("Roll No",shruti) 
    a="shruti"
    print(a," is Present \n")
    present+=1
elif a!=shruti:
    a="shruti"
    print(a,"This is not your Roll Number considered as absent \n")
    absent+=1
    
print("ramya")
a=input("Enter Your Roll Number:")
try:
    a=int(a)
except:
    a="ramya"
    print(a,"Not Answered or Not answered correctly considered as Absent \n")
    absent+=1 
    
if a==ramya:
    print("Roll No",ramya) 
    a="ramya"
    print(a," is Present \n")
    present+=1
elif a!=ramya:
    a="ramya"
    print(a,"This is not your Roll Number considered as absent \n")
    absent+=1
    
print("kavitha")
a=input("Enter Your Roll Number:")
try:
    a=int(a)
except:
    a=0
    
if a==kavitha:
    print("Roll No",kavitha) 
    a="kavitha"
    print(a," is Present \n")
    present+=1
elif a!=kavitha:
    a="kavitha"
    print(a,"This is not your Roll Number considered as absent \n")
    absent+=1

print("Praveen")
a=input("Enter Your Roll Number:")
try:
    a=int(a)
except:
    a="praveen"
    print(a,"Not Answered or Not answered correctly considered as Absent \n")
    absent+=1 
    
if a==praveen:
    print("Roll No",praveen) 
    a="praveen"
    print(a," is Present \n")
    present+=1
elif a!=praveen:
    a="praveen"
    print(a,"This is not your Roll Number considered as absent \n")
    absent+=1
    
print("Students Present ",present)
print("Students Abesnt ",absent)
print("Teacher name is :Praveen")