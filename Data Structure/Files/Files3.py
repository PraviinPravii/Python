

text=open("New Text Document.txt")
for i in text:
    i=i.rstrip()
    if not (i.startswith('From:') or  i.startswith('Name:')):
        print(i)
        continue
    

        