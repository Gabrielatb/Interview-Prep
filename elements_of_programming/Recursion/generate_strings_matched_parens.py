#Write a program that takes as input a number and
#returns all the strings(all possibility => Recursion!)
#with that number of matched pairs of parens.


#n = 1 ---> {'()'}
# n = 2 ---> {'(())', '()()'}
# n = 3 ---> {'((()))', '(()),()', '()()()', '()(())', '(()())'}

# left_needed|| right_needed || valid_prefix || result||
#___________________________________________________
# 3                  3              ''              []

# 2                    3              '('           []

# 1                    3              '(('           []

# XX0                    3              '((()'          []

# XX0                    2              '((()))'          []

# XX0                    1              '((()))'          []
# XX0                    0              '((()))'          ['((()))' ,]

# 1                    2              '(()'           ['((()))' ,]

# 0                    2              '(()('           ['((()))' ,]





#space O(n)
def match_parens(n):
    def helper(left_needed, right_needed, valid_prefix, result=[]):
        print valid_prefix
        print '*************************************************'

        if left_needed > 0:
            #need to insert '('
                helper(left_needed-1, right_needed, valid_prefix + '(')

        if left_needed < right_needed:
            #need to insert '('
                helper(left_needed, right_needed-1, valid_prefix + ')')

        if right_needed == 0:
            result.append(valid_prefix)
        return result


    return helper(n, n, '')


print match_parens(3)