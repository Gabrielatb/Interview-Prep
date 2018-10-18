# Given a string containing digits from 2-9 inclusive,
#  return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons)
#  is given below. Note that 1 does not map to any letters.


def phone(s, phoneNums):

    if len(s) == 0:
        return []
    if len(s) == 1:
        return phoneNums[s[0]]

    prev = phone(s[:-1], phoneNums)

    curr = phoneNums[s[-1]]

    return_lst = []

    for p in prev:
        for c in curr:
            return_lst.append(p+c)

    return return_lst



phoneNums = {'2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']}
s = '356'
print phone(s, phoneNums)