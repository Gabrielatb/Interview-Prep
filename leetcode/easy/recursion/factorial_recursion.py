

#determining factorial through recursion

def factorial(n):

    if n == 1:
        return 1

    return f(n-1) * n


def fib(n):

    if n==0:
        return 0

    if n==1:
        return 1

    return fib(n-1) + fib(n-1) 

def exp(x,n):

    if n==1:

        return x

    return exp(x, n-1) * x



# #calculate x^n using recursion
# #iterative solution
def exponential_iterative(x, n):

    result = 1
    for _ in range(n):
        result *= x  

    return result


