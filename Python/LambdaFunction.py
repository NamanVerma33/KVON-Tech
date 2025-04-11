x = lambda a : a + 5

print(x(5))

y = lambda a,b,c : a * b * c

print(y(2,4,5))

def myFun(n):
    return lambda a : a * n;

doubler = myFun(2)

print(doubler(13))