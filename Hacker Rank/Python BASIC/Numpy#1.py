tuple=tuple()
import numpy
lss=list(map(float,input().split()))
n=int(input())

print(numpy.poly(lss))
print(numpy.roots(lss))
print(numpy.polyint(lss,n))
print(numpy.polyder(lss,n))
print(numpy.polyval(lss, n))
