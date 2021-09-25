#
liss = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]


st=str()
loc=str()
ls=dict()

for i in liss:
    for j in i:
        if str(j).isnumeric():
            loc+=str(j)
        elif j.isalpha():
            st+=str(j)
for i in range(len(st)):
    ls[st[i]]=loc[i]
print(ls)
      
