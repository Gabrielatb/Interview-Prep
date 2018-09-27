#reverse words in string s


def reverse_words(s):

    s_lst = s.split(' ')
    print s_lst




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print '\n****ALL TEST PASSED. YAY!****\n' 
    print reverse_words('Alice likes Bob')