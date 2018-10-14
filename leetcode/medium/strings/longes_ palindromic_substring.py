# Given a string s, find the longest palindromic substring in s.
#You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"


# def longest_palindrome(s):

#     if s == '':
#         return ''


#     reverse_string = reverse(s)
#     print s
#     print reverse_string


#     pal = ''

#     for i in range(len(s)):
#         # print s[i], reverse_string[i]
#         if s[i] == reverse_string[i]:
#             pal = pal + s[i]

#     if pal == '':
#         return None
#     return pal




# def reverse(s):
#     lst = list(s)
#     length = len(lst)

#     for i in range(length/2):
#         temp = lst[i]
#         lst[i] = lst[-(i+1)]
#         lst[-(i+1)] = temp
    
#     final = ''.join(lst)
#     return final


# Time O(n)
# Space O(1)
def longest_palindrome(s):
    """
    :type s: str
    :rtype: str
    """
    for i in reversed(range(len(s))):
        for start in range(len(s)-i):
            substring = s[start: start + i + 1]
            
            if substring == substring[::-1]:
                return substring

#dbbc
print(longest_palindrome('babad'))
















