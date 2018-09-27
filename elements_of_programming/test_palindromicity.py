#for this problem, palindrome is defined is a string that when 
#all non alpha removed reads same front and back

def is_palindome(string):
    """
    >>> is_palindome('a man, a plan, a canal,Panama.')
    True

    >>> is_palindome('Able was I, ere I saw Elba!')
    True

    >>> is_palindome('Ray a Ray')
    False

    """

# Time O(n)
# Space O(1)

    string = [char.lower() for char in string if char.isalpha()]
    for i in range(len(string)/2):
        if string[i] != string[-(i+1)]:
            return False
    return True

# print is_palindome('Able was I, ere I saw Elba!')







if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. WOWZA!\n")