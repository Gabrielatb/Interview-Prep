# Given a string s, find the longest palindromic substring in s.
#You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"


def longest_palindrome(s):
    reverse_string = reverse(s)
    print s
    print reverse_string


    pal = ''

    for i in range(len(s)):
        # print s[i], reverse_string[i]
        if s[i] == reverse_string[i]:
            pal = pal + s[i]

    if pal == '':
        return None
    return pal




def reverse(s):
    lst = list(s)
    length = len(lst)

    for i in range(length/2):
        temp = lst[i]
        lst[i] = lst[-(i+1)]
        lst[-(i+1)] = temp
    
    final = ''.join(lst)
    return final

#dbbc
print(longest_palindrome('cbzd'))
