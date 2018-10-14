# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {}
        dict2 = {}
    
        for char in s:
            if char in dict1:
                dict1[char] +=1 
                
            else:
                 dict1[char]=1 
                    
        for char in t:
            if char in dict2:
                dict2[char] +=1 
                
            else:
                 dict2[char] =1 
                    
        if dict1 == dict2:
            return True
        return False