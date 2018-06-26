#recursion easy problems from Data Structures and Algorithms: Recursion[ 11 exercises with solution]

 # Write a Python program to calculate the sum of a list of numbers

def sum_list_nums(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + sum_list_nums(nums[1:])

# Write a Python program to get the factorial of a non-negative integer.

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Write a Python program to get the sum of a non-negative integer
def sum_int(n):
  if n == 0:
    return 0
  else:
    print n % 10
    print int(n/10)
    return n % 10 + sum_int(int(n / 10))

def harmonic_sum(n):
    if n < 2:
        return 1
    return 1/n + harmonic_sum(n-1)

# Write a Python program to calculate the harmonic sum of n-1.
# Note: The harmonic sum is the sum of reciprocals of the positive integers. 

def power(a,b):
    if b == 1:
        return a
    return a * power(a, b-1)

# Write a Python program to find  the greatest common divisor (gcd) of two integers.

def gcd(a,b):
    def helper(a,b,n):
        if a % n == 0 and b % n == 0:
            return n
        return helper(a,b, n-1)
    if a >= b:
        return helper(a,b, n=b)
    else:
        return helper(a,b, n=a)