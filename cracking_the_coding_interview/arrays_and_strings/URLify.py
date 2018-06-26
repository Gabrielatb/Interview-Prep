###QUESTION 1.3###

#URLify: write method which replaces all spaces in a string with '%20'


def URLify(string, length):
    #mr john smith 
    #[m, r,  , j, o, h, n,  , s, m, i, t, h ]
    string_list = list(string)
    res = []
    
    for i, char in enumerate(string):
        if i > length:
            print 'inside break point'
            break
        elif char == ' ':
            string_list.pop(i)
            string_list.insert(i, '%20')

    for i, char in enumerate(string_list):
        if i < length:
            res.append(char)
        else:
            break

    print len(res), res
    return " ".join(char for char in res)

#time complexity O(n)
#space complexity O(n)

print URLify('Mr John Smith   ', 13)

