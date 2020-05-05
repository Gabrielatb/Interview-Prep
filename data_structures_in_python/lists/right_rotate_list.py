# Given a list, can you rotate its elements by one index from right to left?
# Implement your solution in Python and see if your code runs successfully!


# Problem Statement #
# Implement a function rightRotate(lst,n) which will rotate the given list by k. This means that the right-most elements will appear at the left-most position in the list and so on. You only have to rotate the list by one element at a time.

# Input #
# A list and a number by which to rotate that list

# Output: #
# The given list rotated by k elements

# Sample Input #
# lst = [10,20,30,40,50]
# n = 3
# Sample Output #
# lst = [30,40,50,10,20]

####################################
# My initial brute force solution
####################################
# space: O(n)
# time: o(n**2)
def rightRotate(lst, n):
    while n > 0:
        temp_lst = [0]
        for indx, elem in enumerate(lst):
            if indx == len(lst) - 1:
                temp_lst[0] = elem
            else:
                temp_lst.append(elem)
        lst = temp_lst
        n -= 1
    return lst


####################################
# Solution #1: Manual Rotation
####################################
# space: O(n)
# time: o(n)

def rightRotate(lst, n):
    n = n % len(lst)
    return_lst = []
    for indx in range(len(lst) - n, len(lst)):
        return_lst.append(lst[indx])

    for indx in range(0, len(lst) - n):
        return_lst.append(lst[indx])
    return return_lst


####################################
# Solution #1: List Slicing
####################################
# space: O(n)
# time: O(n)

def rightRotate(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

# [5, 1, 2, 3, 4]
print(rightRotate([1, 2, 3, 4, 5], 1))
# [0, 300, -1, 3]
print(rightRotate([300, -1, 3, 0], 1))
# [2, 0, 0, 0]
print(rightRotate([0, 0, 0, 2], 1))
# ['Python', '13', 'a']
print(rightRotate(['13', 'a', 'Python'], 1))








