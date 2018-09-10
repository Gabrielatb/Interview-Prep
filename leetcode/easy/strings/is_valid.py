"""Is Valid Sentence
Given a dictionary of valid words. Validate that a sentence without
spaces or punctiation consists only of valid words.
Example:
    >>> dictionary = {
            "hello", "hi", "goodbye", "i", "you",
            "me", "we", "is", "am", "are",
            "uber", "ubers", "yes", "no", "maybe",
        }
    >>> is_valid_sentence("iamuber")
    True
    >>> is_valid_sentence("ixam")
    Flase
"""

def is_valid_sentence(s, dict_):
    dict_ = {
            "hello", "hi", "goodbye", "i", "you",
            "me", "we", "is", "am", "are",
            "uber", "ubers", "yes", "no", "maybe",
        }
    is_valid = False
    indx = 0
    while indx < len(s):
        print s
        if s[:indx] in dict_:
            s = s[indx:]
            indx = 0

        

    return is_valid


print is_valid_sentence("iamuber")