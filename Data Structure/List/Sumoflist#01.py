lst=list()
while True:
    fact=input("ENter Factorial Input:")
    if fact=="xit":
       break
    else:
       lst.append(int(fact))
average=sum(lst)/len(lst)
print(lst)
print(average)

       

    