#Design an efficient alg to compute GCD of two non negative int
#solve without using multiplication , div, or modulus operation


 # Euclidean algorithm which is the main algorithm used for this purpose. 
 # The idea is, GCD of two numbers 
 # doesnt change if smaller number is subtracted from a bigger number.



def gcd(a, b):  
    
    #base case for false
    if a == 0 or b == 0:
        return False
    #base case for true
    if a == b:
        return a

    #if a is the greater number
    if a > b:
        return gcd(a-b, b)
    return gcd(a, b-a)


print gcd(6,3) # ---> 3
print gcd(88, 74) # ---> 2
print gcd(24, 108) # ---> 12
print gcd(9, 12) # ---> 3