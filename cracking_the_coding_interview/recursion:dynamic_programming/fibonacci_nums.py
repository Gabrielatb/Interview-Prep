#recursive solution
def fib_1(n):

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_1(n-1) + fib_1(n-2)
# print fib_1(6)

#dynamic programming solution
#top-down
def fib(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n ==2:
        result = 1
    else:
        result = fib(n-1, memo) + fib(n-2, memo)

    memo[n] = result 
    return result

def fib_memo(n):
    memo = [None] * (n + 1)
    return fib(n, memo)

#bottom up
def bottom_up(n): 
    if n ==1 or n==2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]

    return bottom_up[n]


print fib_memo(6)
print fib_1(6)
print bottom_up(6)