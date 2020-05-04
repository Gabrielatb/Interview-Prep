###########################
# Sort and index
###########################
# time: O(nlogn)
# space: O(1)
def findSecondMaximum(lst):
    if len(lst) < 2:
        return None
    lst.sort()
    return lst[-2]

# Caveat: Note that this solution won’t work if duplicates of the first largest number exist. 
# For instance, it would not work with a list like [1,2,4,4] since it would return 4 which is at
# the second last index of the sorted list. But, it is the largest element and not the correct answer.


# print(findSecondMaximum([9, 2, 3, 6])) #expected output: 6
# print(findSecondMaximum([4, 2, 1, 5, 0])) #expected output: 4

###########################
# Traversing the list twice
###########################
# time: O(n)
def findSecondMaximum(lst):
    if (len(lst) < 2):
       return
    first_max = float('-inf')
    second_max = float('-inf')
    for num in lst:
        if num > first_max:
            first_max = num
    for num in lst:
        if num is not first_max and num > second_max:
            second_max = num
    return second_max


# print(findSecondMaximum([9, 2, 3, 6])) #expected output: 6
# print(findSecondMaximum([4, 2, 1, 5, 0])) #expected output: 4


###########################
# Traversing the list twice
###########################
# time: O(n)
def findSecondMaximum(lst):
    if (len(lst) < 2):
       return

    first_max = float('-inf')
    second_max = float('-inf')
    for elem in lst:
        if elem > first_max:
            second_max = first_max
            first_max = elem
        elif first_max > elem > second_max:
            second_max = elem
    return second_max

print(findSecondMaximum([9, 2, 3, 6])) #expected output: 6
print(findSecondMaximum([4, 2, 1, 5, 0])) #expected output: 4