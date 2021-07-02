fl = open ('file.txt')
for l in fl:
     l.rstrip()
     fnd=l.find(".net")
     print(l[fnd+5:fnd+9:])