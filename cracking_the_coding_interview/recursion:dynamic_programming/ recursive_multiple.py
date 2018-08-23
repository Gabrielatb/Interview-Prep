####8.5#######     



def recursive_multiply(int1, int2):

    if int2 == 0:
        return int1

    int1 += int1 
    int2 -=2

    return recursive_multiply(int1, int2)