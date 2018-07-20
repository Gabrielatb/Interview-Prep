#write a method to sort an array of strings so that all the anagrams are next to each other

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #["eat", "tea", "tan", "ate", "nat", "bat"]
        
        #create a dictionary of the anagrams
        
        #{'aet':["eat", "tea", "ate"], "ant":["tan", "nat"], "abt":["bat"]}
        
        
        dict_ = {} 
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            #print sorted_word
            if sorted_word in dict_:
                dict_[sorted_word].append(word)
            else:
                dict_[sorted_word] = [word]
        print dict_
    
        res = []
        for key in dict_:
            res.append(dict_[key])
            
        return res



