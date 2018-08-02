# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.





class Solution(object):
    #max value
    
    #pointer which will be an index

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        max_val = 0
        subst = ''



        for char in s:
            if char not in subst:
                subst += char
                
            else:
                if len(subst) > max_val:
                    max_val = len(subst)
                    
                subst = subst[subst.find(char)+1:]
                subst += char
                
        if len(subst) > max_val:
                max_val = len(subst)
                
        return max_val
                
            
                
