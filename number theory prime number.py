from cmath import sqrt
from math import *
#print(sqrt(73))
#print(round(sqrt(73)))
def func(n):
    print(sqrt(n))
    if n == 0 or n ==1:
        return False
    if n == 2 or n == 3:
        return True
    if n%2 ==0 and n%3==0:
        return False
    for elm in range(5,int(sqrt(n))+1,4):
        if n% elm ==0 or n % (elm+2) == 0:
            return False
    return True
#print(sqrt(73))
print(func(75))
