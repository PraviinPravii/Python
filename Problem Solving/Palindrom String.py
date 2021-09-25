a="sqfopldohhwnbhhpnbxiwzvkybggkgtftvvaqpejznlxluatcppctaulxlnzjepqavvtftgkggbykvzwixbnphhbnwhhodlpofqs"
st1=str()
st2=str()
for i in range(int(len(a)/2)):
    st1+=a[i]
    j=i
for i in range(j+1,len(a)):
    st2+=a[i]
if st1==st2[::-1]:
    print("YES")
else:
    print("NO")
    

    





