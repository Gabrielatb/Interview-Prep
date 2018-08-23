####8.5#######  
 



####Initial Solution#####
def recursive_multiply(int1, int2):
    """"
    >>> recursive_multiply(3, 2)
    6
    >>> recursive_multiply(2, 3)
    6
    >>> recursive_multiply(6, 6)
    36
    >>> recursive_multiply(9, 7)
    63
    >>> recursive_multiply(0, 100)
    0
    >>> recursive_multiply(100, 0)
    0
    """

    if int1 < int2:
        int1, int2 = int2, int1

    return multiply(int1, int2, total=0)


def multiply(int1, int2, total):
    if int2 == 0:
        return total

    total += int1 
    int2 -=1

    return multiply(int1, int2, total)




if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All Tests Passed YAY!"