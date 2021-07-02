color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color1=['Blue','Orange','White','Yello','Dark Green']
colorz = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
colorr=[i for j,i in enumerate(color) if i in (color1)]
print(colorz)
print(colorr)

print([x for (x,i) in enumerate(color)],[x for (i,x) in enumerate(color)])

