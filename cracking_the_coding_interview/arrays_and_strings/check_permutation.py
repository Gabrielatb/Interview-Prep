# Given two strings, write a method to decide if one is a permutation of the other

#approach: creat dictionary for each string with key being letter, value be how many
# time that letter appeared in the word
#compare dictionaries at the end

def is_permutation(s1, s2):

#     s1 = s1.lower()
#     s2 = s2.lower()
#     dict1 = {}
#     dict2 = {}

#     for char in s1:
#         if char in dict1:
#             dict1[char] += 1

#         else:
#             dict1[char] = 1

#     for char in s2:
#         if char in dict2:
#             dict2[char] += 1

#         else:
#             dict2[char] = 1

#     if dict1 == dict2:
#         return True

#     return False

# print is_permutation('abc', 'bca')
# print is_permutation('top', 'pot')
# print is_permutation('abc', 'ajskldajdlkas')

#time complexity O(n**2)
#space complexity 0(n**2)

#################################################################################

#     s1_sorted = sorted(s1)
#     s2_sorted = sorted(s2)

#     if s2_sorted == s1_sorted:
#         return True

#     return False

# print is_permutation('abc', 'bca')
# print is_permutation('top', 'pot')
# print is_permutation('abc', 'ajskldajdlkas')

# time complexity nlogn
# space complexity O(n)

#################################################################################

    char_list = []

    for char in s1:
        char_list.append(char)

    for char in s2:
        if char not in char_list:
            return False
        else:
            char_list.remove(char)

    if len(char_list) == 0:
        return True
    return False

print is_permutation('abc', 'bca')
print is_permutation('top', 'pot')
print is_permutation('abc', 'ajskldajdlkas')


time complexity O(n**2)
space complexity O(n)

