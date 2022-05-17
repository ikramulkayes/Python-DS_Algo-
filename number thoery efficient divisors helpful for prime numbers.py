from cmath import sqrt
from math import *


def fun2(n):
    print(sqrt(n))
    word = set()
    for i in range(1,int(sqrt(n))+1):
        if n %i == 0:
            word.add(i)
            word.add(n//i) # if i = 2 and n = 24 so n/i = 12 is also a divisor of n
    return list(word)

print(*fun2(73))