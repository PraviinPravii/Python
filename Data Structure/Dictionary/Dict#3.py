dic=dict()
strg="Googlewww.google.com Search the world's the information, including webpages, images,"
"More results from google.com »"
strspl=strg.split()
for ls in strspl:
    dic[ls]=dic.get(ls,0)+1
print(dic)