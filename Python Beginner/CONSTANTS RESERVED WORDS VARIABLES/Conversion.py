# implicit Conversion
floatsum=22+28.0#integer value is implicitly converted to float
intsum=22+28 #if both are integer nothing will happen
print(floatsum,intsum)
#string converstion
string="445"
strfloat=float(string)##string 445 is converted to float of 445.0
strint=int(string)#string 445 is converted to integer of 445
print(strfloat)
print(strint)
"""Any Alphabetic strings are cannot be converted it will give you traceback as below

 strfloat=float(string)##string 445 is converted to float of 445.0

ValueError: could not convert string to float: 'Hello Im alpha'
"""