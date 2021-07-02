time="11:21:30 PM"
convert=0
if int(time[:2])<12 and time[-2:]=="AM":
    print(time)
elif time[-2:]=="PM" and int(time[:2])>=1 and int(time[:2])<12:
    print(int(time[:2])+12,time[2:8])
elif int(time[:2])>=12 and time[-2:]=="PM":
    print(time[0:8])
elif int(time[:2])>=12 and time[-2:]=="AM":
    print("00",time[2:8],"AM")
else:
    print("Enter Correct time format 12 Hour")
