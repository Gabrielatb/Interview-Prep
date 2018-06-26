#determining factorial through recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

#fibonacci numbers through recursions
def fib(n):
    if n == 0:
        return 1
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


#calculate x^n using recursion
#iterative solution
def exponential_iterative(x, n):

    result = 1
    for _ in range(n):
        result *= x  

    return result
def exponential_recursive(x, n):

    if n == 0:
        return 1
    else:
        return x * exponential_recursive(x, n-1)

