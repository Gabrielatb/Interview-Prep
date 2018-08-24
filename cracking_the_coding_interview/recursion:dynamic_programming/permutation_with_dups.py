####8.8#####

#permutation with duplicates

# def permutation(word):

#     if word == None:
#         return None

#     result = []
#     if len(word) == 0:
#         result.append('')
#         return result

#     first = word[0]
#     print "this is first ", first
#     remainder = word[1:]
#     print "this is remainder ", remainder

#     perm = permutation(remainder)
#     print 'this is a permutation ', perm


#     for word in perm:
#         print 'this is a word',  word
#         for i in range(len(word)+1):
#             result.append(insert(word, first, i))

#     return result


# def insert(word, char, i):
#     print "this is the combined word ", word[:i] + char + word[i:]
#     return word[:i] + char + word[i:]