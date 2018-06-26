# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    index_list = []
    j = 0
    for i in range(len(haystack)):
        print "these are the indexes " + str(i) + " " + str(j)
        print haystack[i], needle[j]
        if haystack[i] == needle[j]:
            index_list.append(i)
            print index_list
            if j < len(needle) -1:
                j += 1
    if len(index_list) >= len(needle):
        return index_list[0]
    return -1


# print strStr("hello", "ll")
# print strStr("aaaaa", "bba")
print strStr("aaa", "a")