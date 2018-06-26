#is palindrome recursive solution

    # iterative solution
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    count = 0
    s = ''.join([char for char in s if char.isalpha() or char.isdigit()])
    print s
    s = s.lower()
    print s
    for i in range(len(s)/2):
            if s[i] == s[-(i+1)]:
                count += 1
    if count == (len(s)/2):
        return True
    return False

    # recursive solution
def isPalindrome(s):
    def isChar(s):
        s = ''.join([char for char in s if char.isalpha() or char.isdigit()])
        s = s.lower()
        return s
    


    def isPal(s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(isChar(s))

