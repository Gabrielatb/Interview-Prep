# Count the number of prime numbers less than a non-negative number, n



def count_prime(n):

    count = 0
    prime = [True for i in range(n+1)]
    p = 2

    while p * p <= n:
        if prime[p] == True:
            for i in range(p*2, n+1, p):
                prime[i] = False

        p +=1 

    for i in range(2,n):
        if prime[i]:
            count +=1 

    return count


