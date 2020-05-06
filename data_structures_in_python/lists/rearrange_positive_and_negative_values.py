# Problem Statement #
# Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear on the left and positive elements appear at the right of the list. Note that it is not necessary to maintain the order of the input list.

# Generally zero is NOT positive or negative, we will treat zero as a positive integer for this challenge! So, zero will be placed at the right.

# Output #
# A list with negative elements at the left and positive elements at the right

# Sample Input #
# [10,-1,20,4,5,-9,-6]
# Sample Output #
# [-1,-9,-6,10,20,4,5]

########################
# Brute Force
########################
# Time: O(n)
# Space: O(n)
# def rearrange(lst):

#     pos = []
#     neg = []
#     for elem in lst:
#         if elem < 0:
#             neg.append(elem)
#         else:
#             pos.append(elem)
#     return neg + pos

########################
# Solution #2: Rearranging in Place
########################
# Time: O(n)
# Space: O(1)
# def rearrange(lst):
#     leftMostPosNum = 0
#     for indx in range(len(lst)):
#         if lst[indx] < 0:
#             # swap
#             if (leftMostPosNum != indx):
#                 lst[indx], lst[leftMostPosNum] = lst[leftMostPosNum], lst[indx]
#             leftMostPosNum += 1
#     return lst

########################
# Solution #3: Pythonic Rearrangemen
########################
# Time: O(n)
# Space: O(n)
def rearrange(lst):
    return [elem for elem in lst if elem < 0] + [elem for elem in lst if elem >= 0]

# [-1, -3, -4, 2, 5]  
print(rearrange([-1, 2, -3, -4, 5]))
# [-1, 300, 3, 0]
print(rearrange([300, -1, 3, 0]))
# [-2, 0, 0, 0]
print(rearrange([0, 0, 0, -2]))
