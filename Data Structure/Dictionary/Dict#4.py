dic=dict()
strg="Google, LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware. Wikipedia"
lst=strg.split()

for ls in lst:
    dic[ls]=dic.get(ls,0)+1
    lsst=list(dic.items())

print(lsst[5])

    