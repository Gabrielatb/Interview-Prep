# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.



#["flower","flow","flight"]
def longest_prefix(lst):
    # min_indx = 0
    min_word = min(lst, key=len)

    length_lst = []

    prefix = ''

    i = 0
    count = 0

    #Time Complexity: O(nn) 
    #Space Complexity: O(n)
    while i <= len(min_word) -1:
        for word in lst:
            if word[i] == min_word[i]:
                count +=1
        if count == len(lst):
            prefix += min_word[i]
            i+=1
            count = 0
        else:
            return prefix
    return prefix





print longest_prefix(["flower","flow","flight"])