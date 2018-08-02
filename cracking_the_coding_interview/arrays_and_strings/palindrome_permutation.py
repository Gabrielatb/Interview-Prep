#Given a string, write a function to check if it is a permutation
#of a palindrome.


#input: Tact Coa

#permutation same amount of letters in word

def palindrome_permutation(strng):

    lst1 = []
    lst2 = []

    strng = strng.lower()
    string = strng.replace(" ", "")
    string = sorted(string)

    for char in string:
        if char not in lst1:
            lst1.append(char)
        else:
            lst2.append(char)

    if lst1 == lst2 or len(lst1) - len(lst2) == 1:
        return True
    return False












print palindrome_permutation("Tact Coa")
print palindrome_permutation("Amenc cy inemai")























# def palindrome(str_):

#     _str = " ".join(s for s in str_ if s.isalpha() or s.isdigit())

#     for i in range(len(_str)/2):
#         if _str[i] != _str[-(i+1)]:
#             return False
#         else:
#             continue

#     return True




# print palindrome('race     car....')