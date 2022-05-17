from math import *

def func(n):
    #flst = []
    lst = [True]*(n+1)
    lst[0] = False
    lst[1] = False
    for elm in range(2,int(sqrt(n))+1): # as 
        if lst[elm] == True:
            for i in range(elm*elm,n+1,elm):  # just run it deleting the elemnts by the prime numbers as for elm = 2 range will start from 4,6, 8 and for 3 it will start 9, 12, 15
                if i % elm == 0:
                    lst[i] = False
    for elm in range(0,n+1):
        if lst[elm] == True:
            print(elm,end=" ")
    return ""
k = int(input())
print(func(k))
