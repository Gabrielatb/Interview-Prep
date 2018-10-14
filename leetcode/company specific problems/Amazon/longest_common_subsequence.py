# LCS Problem Statement: Given two sequences, find the length of longest subsequence
# present in both of them. A subsequence is a sequence that appears in the same
# relative order, but not necessarily contiguous.

#Time O(n)
#Space O(n)
def longest_sub(s1, s2):
#     #recursive solution
#     if i >= len(s1):
#         print result
#         return len(result)
    
#     if s1[i] in s2:
#         print s1[i]
#         result += s1[i]
#         index_s2 = s2.find(s1[i])
#         s2 = s2[index_s2+1:]
#     i+=1

#     return longest_sub(s1, s2, i, result)
# def initial(s1, s2):
#     if len(s2) < len(s1):
#         s1, s2 = s2, s1

#     return longest_sub(s1, s2, 0, '')


    #iterative solution
    #guranteed that s1 is always bigger string
    print len(s2)
    print len(s1)
    if len(s2) > len(s1):
        s1, s2 = s2, s1

    result = ''
    for char in s1:
        print 'all chars ', char
        if char in s2:
            print 'special char ', char
            result +=char
            index_s2 = s2.find(char)
            s2 = s2[index_s2+1:]
    print result
    return len(result)

[(A, 5)]
'AGGTABB', 'GXTXAYB')
# print longest_sub("ABCDGH", "AEDFHR")
print longest_sub('AGGTABB', 'GXTXAYB')
#'GTAB' of length 4.