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

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""

    def compare(small, big):
        same = ""
        for indx in range(len(small)):
            if small[indx] == big[indx]:
                same += small[indx]
            else:
                return same
        return same
            
    return_string = strs[-1]
    for indx in range(len(strs) -1):
        if len(return_string) < len(strs[indx]):
            return_string = compare(return_string, strs[indx])
        else:
            return_string = compare(strs[indx], return_string)
    return return_string