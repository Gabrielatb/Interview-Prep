# Write a function that takes a string as input and returns the string reversed.

# Example:
# Given s = "hello", return "olleh".


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_lst = []
        for char in s[::-1]:
            str_lst.append(char)
            
        return ''.join(str_lst)