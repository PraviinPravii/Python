import time

print("Loading...Please wait for 5 seconds loading latitude longitude and thier water levels")
for x in range (5):
    print(x+1)
    time.sleep(1)

latitude = ([14.12,14.21,14.51,15.32,16.43], [17.45,18.46 ,18.79,19.10,20.22], [22.26,23.56,26.55,27.56,29.64])

longitude = ([74.12,75.21,75.51,76.77 ,77.43], [78.45,79.46 ,79.79,80.10,81.22], [86.26,87.56,88.55,89.56,90.64 ])

waterslevel=[[67,70,56,0,30],[70,0,80,49,35],[98,78,84,30,0]]

print("These are the places available shown as langitude and latitude and the water levels")

print("\n")
print("In the district first taluk and thier latitude longitude and their water levels")
print("\n")
for x in range (2):
    time.sleep(1)
print("latitude",latitude[0][0],"longitude",longitude[0][0],"| Water level is ",waterslevel[0][0],"%")
for x in range (2):
    time.sleep(1)
print("\n")
print("latitude",latitude[0][1],"longitude",longitude[0][1],"| Water level is ",waterslevel[0][1],"%")
for x in range (2):
    time.sleep(1)
print("\n")
print("latitude",latitude[0][2],"longitude",longitude[0][2],"| Water level is ",waterslevel[0][2],"%")
for x in range (2):
    time.sleep(1)
print("\n")
print("latitude",latitude[0][3],"longitude",longitude[0][3],"| Not Measured")
for x in range (2):
    time.sleep(1)
print("\n")
print("latitude",latitude[0][4],"longitude",longitude[0][4],"| Water level is ",waterslevel[0][4],"%")
for x in range (2):
    time.sleep(1)
print("\n")



print("\n")
print("Loading... second taluk and thier latitude longitude and their water levels")
print("\n")
print("latitude",latitude[1][0],"longitude",longitude[1][0],"| Water level is ",waterslevel[1][0],"%")
for x in range (2):
    time.sleep(1)
print("\n")
print("latitude",latitude[1][1],"longitude",longitude[1][1],"|  Not Measured")
for x in range (2):
    time.sleep(1)
print("\n")
print("latitude",latitude[1][2],"longitude",longitude[1][2],"| Water level is ",waterslevel[1][2],"%")
for x in range (2):
    time.sleep(1)
print("\n")
print("latitude",latitude[1][3],"longitude",longitude[1][3],"| Water level is ",waterslevel[1][3],"%")
for x in range (2):
    time.sleep(1)
print("\n")
print("latitude",latitude[1][4],"longitude",longitude[1][4],"| Water level is ",waterslevel[1][4],"%")
for x in range (2):
    time.sleep(1)
print("\n")


print("\n")
print("In the district third taluk and thier latitude longitude and their water levels")

print("latitude",latitude[2][0],"longitude",longitude[2][0],"| Water level is ",waterslevel[2][0],"%")
for x in range (2):
    time.sleep(1)
print("\n")
print("latitude",latitude[2][1],"longitude",longitude[2][1],"| Water level is ",waterslevel[2][1],"%")
for x in range (2):
    time.sleep(1)
print("\n")
print("latitude",latitude[2][2],"longitude",longitude[2][2],"| Water level is ",waterslevel[2][2],"%")
for x in range (2):
    time.sleep(1)
print("\n")
print("latitude",latitude[2][3],"longitude",longitude[2][3],"| Water level is ",waterslevel[2][3],"%")
for x in range (2):
    time.sleep(1)
print("\n")
print("latitude",latitude[2][4],"longitude",longitude[2][4],"|  Not Measured")
for x in range (2):
    time.sleep(1)
print("\n")

print("These are the empty places to construct home in this longitude and latitude :")
print("\n")

print("First Empty Place")
print(latitude[0][3]," Latitude")
print(longitude[0][3], " Longitude")
for x in range (3):
    time.sleep(1)
print("\n")

print("Second Empty  Place")
print(latitude[1][1]," Latitude")
print(longitude[1][1], " Longitude")
for x in range (3):
    time.sleep(1)
print("\n")
print("Third empty Place")
print(latitude[2][4], " Latitude")
print(longitude[2][4]," Longitude")
for x in range (3):
    time.sleep(1)
print("\n")

latude=float(input("Enter the Latitude :"))
lotude=float(input("Enter the longitude:"))
print("\n")
if latude==latitude[0][3] and lotude==longitude[0][3]:
    avg = sum(waterslevel[0])/len(waterslevel[0])
    print("The Chances of water came in lake this place :",avg,"%")
if latude==latitude[1][1] and lotude==longitude[1][1]:
    avg = sum(waterslevel[1])/len(waterslevel[1])
    print("The Chances of water came in lake this place :",avg,"%")
if latude==latitude[2][4] and lotude==longitude[2][4]:
    avg = sum(waterslevel[2])/len(waterslevel[2])
    print("The Chances of water came in lake this place :",avg,"%")
    
