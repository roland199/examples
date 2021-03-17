#python translation of fib.cc
def fib_recursive(n):
if (n ==1 or n==2):
    return 1
else:
    return(fib_recursive(n-1)+fib_recursive(n-2))


def fib_iterative(n):
    a = 1
    b = 1
    i = 3
    temp = 0
    if (n == 1 or n ==2):
        return 1
    for i in range (6):
        temp = b
        b = a + b
        a = temp
    return b