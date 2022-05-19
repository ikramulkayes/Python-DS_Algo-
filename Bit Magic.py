def evenodd(x):
    if x&1 ==1:
        return("ODD")
    else:
        return("EVEN")  #it is just to find even odd numbers
def mul(x,y):
    return x<<y # x^(2*y)
def div(x,y):
    return x>>y # it is the inverse x ^ - (2*y)

x,y = map(int,input().split())
print(f"{x} is {evenodd(x)} and mul is {mul(x,y)} and div is {div(x,y)} ")
