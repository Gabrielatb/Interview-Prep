#problem 1.6




def string_compression(strng):

    curr_letter = None
    count = 0

    result = []
    for char in strng:
        if curr_letter is None:
            curr_letter = char
            count = 1

        elif curr_letter != char:
            result.append(curr_letter)
            result.append(str(count))
            curr_letter = char
            count = 1

        else:
            count += 1

    result.append(curr_letter)
    result.append(str(count))

    if len(result) > len(strng):
        return strng

    res = " ".join( char for char in result)
    return res





print string_compression('aabcccccaaa')
print string_compression('abc')