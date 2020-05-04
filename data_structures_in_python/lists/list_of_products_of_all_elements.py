# Problem Statement #
# Implement a function, findProduct(lst),
# which modifies a list so that each index has a product
# of all the numbers present in the list except the number
# stored at that index.

# Input: #
# A list of numbers (could be floating points or integers)

# Output: #
# A list such that each index has a product of all the numbers in the list except the number stored at that index.

# Sample Input #
# arr = [1,2,3,4]
# Sample Output #
# arr = [24,12,8,6]
# time: O(n^2)
# space: O(n)
###############################
# Initial BRUTE FORCE APPROACH
###############################
def returnLeftProduct(indx, lst):
    left_product = 1
    while indx >= 0:
        left_product *= lst[indx]
        indx -= 1
    return left_product

def returnRightProduct(indx, lst):
    right_product = 1
    while indx < len(lst):
        right_product *= lst[indx]
        indx +=1
    return right_product

def findProduct(lst):
    result_lst = []
    left
    for indx in range(len(lst)):
        total_product = 1
        left_product = 1
        right_product = 1
        if indx - 1 >= 0:
            left_indx = indx - 1
            left_product = returnLeftProduct(left_indx, lst)
        if indx + 1 < len(lst):
            right_indx = indx + 1
            right_product = returnRightProduct(right_indx, lst)
        total_product = left_product * right_product
        result_lst.append(total_product)
    return result_lst

print(findProduct([2, 5, 9, 3, 6]))
print(findProduct([1, 2, 3, 4]))


###############################
# Using a nested loop
###############################
# space complexity: O(n)
# time complexity: O(n^2)
def findProduct(lst):
    [1, 2, 3, 4]
    result_lst = []
    left = 1
    for i in range(len(lst)):
        right_sum = 1
        for elem in lst[i+1:]:
            right_sum *= elem
        result_lst.append(right_sum * left)
        left *= lst[i]
    return result_lst

# [24, 12, 8, 6]
# [810, 324, 180, 540, 270]
print(findProduct([2, 5, 9, 3, 6]))
print(findProduct([1, 2, 3, 4]))

##########################################
# Optimizing the number of multiplications
##########################################
# Space Complexity: O(n)
# Time Complexity: O(n)
def findProduct(lst):
    left = 1
    final_product = []
    for elem in lst:
        final_product.append(left)
        left *= elem


    right = 1
    for indx in range(len(lst) - 1, -1, -1):
        final_product[indx] *= right
        right *= lst[indx]

    return final_product


# [24, 12, 8, 6]
# [810, 324, 180, 540, 270]
print(findProduct([2, 5, 9, 3, 6]))
print(findProduct([1, 2, 3, 4]))
