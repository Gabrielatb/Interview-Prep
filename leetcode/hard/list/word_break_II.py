# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
 # add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:

# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:[]



def word_break(s, wordDict):
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]


    return_lst = []

    for word in wordDict:
        if s.startswith(word):
            i = len(word)
            temp = s[i:]
            poss_breaks = word_break(temp, wordDict)
            if poss_breaks:
                for poss_break in poss_breaks:
                    print poss_break
                    return_lst.append(word + ' ' + poss_break)
            else:
                return_lst.append(word)

    return return_lst


vocab = {
'a',
'ate',
'dinner',
'for',
'ford',
'i',
'inner',
'night',
'noodles',
'oodles',
'ten',
'to',
'tonight'
}


print word_break("atenoodles", vocab)






