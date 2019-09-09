# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

# Example 1:

# Input: "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"
# Example 2:

# Input: "aeiou"
# Output: ""

def removeVowels(S):
    no_vowels = ""
    
    for char in S:
        if char not in ['a', 'e', 'i', 'o', 'u']:
            no_vowels += char
    return no_vowels