# implement run-length encoding and decoding


# 'aaaabcccaa' --> 4a1b3c2a

def encoding(s):
    """"
    >>> encoding('aaaabcccaa')
    '4a1b3c2a'

    >>> encoding('')
    ''

    """
    if s == '':
        return s

    encoded = ''

    prev = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == prev:
            count += 1

        else:
            encoded += str(count) + prev
            count = 1
            prev = s[i]

    encoded += str(count) + prev
    return encoded

def decoding(s):
    """"
    >>> decoding('3e4f2e')
    'eeeffffee'

    >>> decoding('')
    ''

    """

    decoded = ''

    if s == '':
        return ''

    for indx, elem in enumerate(s):
        if elem.isdigit() == True:
            num = int(elem)
            while num > 0:
                decoded += s[indx+1]
                num -= 1


    return decoded

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print '\n**** All tests passes****!\n'

