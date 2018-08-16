# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true


def isValid(s):
    """

    >>> isValid("()")
    True

    """


    dict_ = {')': '(', '}': '{', ']': '['}

    seen = []

    for para in s:
        if para in [')', '}', ']']:
            if len(para) == 0 or seen[-1] != dict_[para]:
                return False
            else:
                seen.pop()
        else:
            seen.append(para)
    if len(seen) ==0:
        return True
    return False





if __name__ == "__main__":
    import doctest
    doctest.testmod()
            
