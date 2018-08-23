#####8.7#######


#Write a method which computers all permutations of a string of unique char


#run time )(n**2 * n!)

def permutation(word):

    if word == None:
        return None

    result = []
    if len(word) == 0:
        result.append('')
        return result

    first = word[0]
    print "this is first ", first
    remainder = word[1:]
    print "this is remainder ", remainder

    perm = permutation(remainder)
    print 'this is a permutation ', perm


    for word in perm:
        print 'this is a word',  word
        for i in range(len(word)+1):
            result.append(insert(word, first, i))

    return result


def insert(word, char, i):
    print "this is the combined word ", word[:i] + char + word[i:]
    return word[:i] + char + word[i:]





# def perm(str):
#     if str == None:
#         return None
        
#     result = []
#     if len(str) == 0:
#         result.append("")
#         return result
        
#     first = str[0]
#     remainder = str[1:len(str)]
    
#     # This recursively gets permutations from the remainder, so it starts at the empty string
#     permutations = perm(remainder)
#     print permutations
    
#     # For every permutations
#     for word in permutations:
#         # print word
#         # For every possible index in each permutation
#         for i in range(len(word)+1):
#             # Add the new letter to every index to generate new set of permutations
#             result.append(insertAt(word, first, i))

#     return result
    
        

# def insertAt(str, c, idx):
#     return str[:idx] + c + str[idx:len(str)]
