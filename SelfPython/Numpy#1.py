import numpy as np

array_num=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[3,34,33,4]]

arry=np.array(array_num)
print(arry)
print(arry.shape)
a=int(len(arry)*len(arry[0])/2)
print(arry.reshape(2,a))
ary=np.arange(-10,10,1)
print(ary)