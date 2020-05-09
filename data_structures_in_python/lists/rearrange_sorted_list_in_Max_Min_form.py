# Problem Statement #
# Implement a function called maxMin(lst) which will re-arrange the elements of a sorted list such that the first position will have the largest number, the second will have the smallest, and the third will have second largest, and so on. In other words, all the odd-numbered indices will have the largest numbers in the list in descending order and the even numbered indices will have the smallest numbers in ascending order.

# Input: #
# A sorted list

# Output: #
# A list with elements stored in max/min form

# Sample Input #
# lst = [1,2,3,4,5]
# Sample Output #
# lst = [5,1,4,2,3]

###################################
# Initial Brute Force Approach
###################################
# Time: O(n)
# Space: O(n)
def maxMin(lst):
    half_len_lst = len(lst) // 2
    return_lst = []
    for indx in range(half_len_lst):
        return_lst.append(lst[-(indx + 1)])
        return_lst.append(lst[indx])
    if len(lst) % 2 != 0:
        return_lst.append(lst[half_len_lst])
    return return_lst

###################################
# Using O(1)O(1) Extra Space 
###################################
# time: o(n)
# space: O(1)
# Note: This approach only works for non-negative numbers!
def maxMin(lst):
    if len(lst) == 0:
        return []

    minIndx = 0
    maxIndx = len(lst) -1
    maxElem = lst[maxIndx] + 1
    for indx in range(len(lst)):
        if indx % 2 == 0:
            lst[indx] += (lst[maxIndx] % maxElem) * maxElem
            maxIndx -=1
        else:
            lst[indx] += (lst[minIndx] % maxElem) * maxElem
            minIndx += 1
    for indx in range(len(lst)):
        lst[indx] = lst[indx] // maxElem
    return lst

# [7, 1, 6, 2, 5, 3, 4]   
print(maxMin([1, 2, 3, 4, 5, 6, 7]))
# [5, 1, 4, 2, 3]
print(maxMin([1, 2, 3, 4, 5]))
# []
print(maxMin([]))
# [1, 1, 1, 1, 1]
print(maxMin([1, 1, 1, 1, 1]))
# [1, -10, 1, -1, 1, 1]
print(maxMin([-10, -1, 1, 1, 1, 1]))