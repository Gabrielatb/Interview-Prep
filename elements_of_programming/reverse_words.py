#reverse words in string s


def reverse_words(s):
    """
    >>> reverse_words('Bob likes Alice')
    'Alice likes Bob'

    """

    s_lst = s.split(' ')

    for i in range(len(s_lst)/2):
        s_lst[i], s_lst[-(i+1)] = s_lst[-(i+1)], s_lst[i]
   
    return ' '.join(s_lst)





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print '\n****ALL TEST PASSED. YAY!****\n' 
   