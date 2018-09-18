#is palindrome recursive solution

#racecar --> True

#f(e) -> return True
#f(cec) - >return True
#f(aceca) -> return True
#f(racecar) -> return True



#f(us) - >return False
#f(ouse) -> return False
#f(house) -> return False



#house --> False

#recursive solution
def pal(word):

    if len(word) <= 1:
        return True

    else:

        return pal(word[1:-1]) and word[0] == word[-1]



#iterative
def pal_iterative(word):

    for i in range(len(word)/2):
        if word[i] != word[-(i+1)]:
            return False
    return True


print pal_iterative('racecar')
print pal_iterative('raceca')
























    # iterative solution
# def isPalindrome(s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     count = 0
#     s = ''.join([char for char in s if char.isalpha() or char.isdigit()])
#     print s
#     s = s.lower()
#     print s
#     for i in range(len(s)/2):
#             if s[i] == s[-(i+1)]:
#                 count += 1
#     if count == (len(s)/2):
#         return True
#     return False

#     # recursive solution
# def isPalindrome(s):
#     def isChar(s):
#         s = ''.join([char for char in s if char.isalpha() or char.isdigit()])
#         s = s.lower()
#         return s
    


#     def isPal(s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         if len(s) <= 1:
#             return True
#         else:
#             return s[0] == s[-1] and isPal(s[1:-1])
#     return isPal(isChar(s))

