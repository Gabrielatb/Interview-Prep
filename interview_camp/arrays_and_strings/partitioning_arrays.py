# Level: Easy
# You are given an array of integers. Rearrange the array so that all zeroes are at the beginning of the array. For example, a = [4,2,0,1,0,3,0] -> [0,0,0,4,1,2,3]
#E S T C V

#[0,0,4,1,2,3,0]

#questions:
# Are we guranteed just numbers
# What happens if the array is empty
# What happens if there are no zeros -> array remains unchanges
# Do the non-zero numbers need to be in the same order when we return 

#Edge cases: [], null, [1,2,3], [0,0,0]
#base cases: [6,0], [0, 2]
#regular cases: [1,0,3,6,7], [1,0,0,0]
def swap(indx, boundary, lst):
    temp = lst[indx]
    lst[indx] = lst[boundary]
    lst[boundary] = temp

def partition_array_zeros_at_beg(lst):
    if lst == None or len(lst) == 0:
        return lst

    boundary = 0
    for indx in range(len(lst)):
        num = lst[indx]
        if num == 0:
            swap(indx, boundary, lst)
            boundary +=1
    return lst
# time: O(n)
# space: O(1)
# print(partition_array_zeros_at_beg([1,0,3,6,7]))
# print(partition_array_zeros_at_beg([1,0,0,0]))
# print(partition_array_zeros_at_beg([0, 2]))
# print(partition_array_zeros_at_beg([6,0]))
# print(partition_array_zeros_at_beg([]))
# print(partition_array_zeros_at_beg(None))
# print(partition_array_zeros_at_beg([1,2,3]))
# print(partition_array_zeros_at_beg([0,0,0]))
#############################################

def partition_array_zeros_at_end(lst):
    if lst == None or len(lst) == 0:
        return lst

    boundary = len(lst) -1
    for indx in range(len(lst) -1, -1, -1):
        num = lst[indx]
        if num == 0:
            swap(indx, boundary, lst)
            boundary -=1
    return lst

# time: O(n)
# space: O(1)
# print(partition_array_zeros_at_end([1,0,3,6,7]))
# print(partition_array_zeros_at_end([1,0,0,0]))
# print(partition_array_zeros_at_end([0, 2]))
# print(partition_array_zeros_at_end([6,0]))
# print(partition_array_zeros_at_end([]))
# print(partition_array_zeros_at_end(None))
# print(partition_array_zeros_at_end([1,2,3]))
# print(partition_array_zeros_at_end([0,0,0]))

# Problem: Dutch National FlagLevel: Medium
# You are given an array of integers and a pivot. 
# Rearrange the array in the following order:[all elements less than pivot, elements equal to pivot, elements greater than pivot]
# For example, a = [5,2,4,4,6,4,4,3] and pivot = 4 --> result = [3,2,4,4,4,4,5,6].

# Questions I would ask:
# Are we guranteed just numbers?
# Are we guranteed that the pivot will be in the array? No.
# What happens if the array is null or empty
# Do the numbers on each side need to be sorted? No.
# What if there are no numbers less than pivot or greater than pivot?
#Does the order of the numbers before and after pivot matter?

# Edge cases: [], None, pivot is not in the array
# Base case: [4], [2,3]
# Regular case: [5,3,4], [5,3,4,4,4], [3,2,4,4,4,4,5,6], [4,4,4,4,5,6], [3,2,4,4,4,4], [3,5,4], [3,5,4,4,4]

[3,2,4,4,6,4,4,5]

#if num is less than pivot
    # swap with low boundary
    # low boundary +=1
    # indx +=1

#if num is greater than pivot
    # swap with high boundary
    # high boundary = -1

#if number is equal to pivot
    # increase index
    # indx += 1 

def dutch_national_flatg(lst, pivot):
    if lst == None or len(lst) == 0:
        return lst

    indx = 0
    high_boundary = len(lst) -1
    low_boundary = 0
    while indx <= high_boundary:
        num = lst[indx]
        if num < pivot:
            swap(indx, low_boundary, lst)
            low_boundary += 1
            indx += 1
        elif num > pivot:
            swap(indx, high_boundary, lst)
            high_boundary -= 1
        else:
            indx += 1

    return lst

# print(dutch_national_flatg([5,2,4,4,6,4,4,3], 4))
# print(dutch_national_flatg([], 4))
# print(dutch_national_flatg(None, 4))
# print(dutch_national_flatg([5,2,3], 4))
# print(dutch_national_flatg([4], 4))
# print(dutch_national_flatg([2,3], 4))
# print(dutch_national_flatg([5,3,4,4,4], 4))
# print(dutch_national_flatg([3,2,4,4,4,4,5,6], 4))
# print(dutch_national_flatg([3,2,4,4,4,4], 4))
# print(dutch_national_flatg([3,5,4], 4))
# print(dutch_national_flatg([3,5,4,4,4], 4))

# Homework Problem (Level: Medium)
# Given an array with n marbles colored Red, White or Blue, sort them so that marbles of the same color are adjacent, with the colors in the order Red, White and Blue.
# Assume the colors are given as numbers - 0 (Red), 1 (White) and 2 (Blue).
# For example, if A = [1,0,1,2,1,0,1,2], Output = [0,0,1,1,1,1,2,2].

# Are guranteed only those number will appear in the array, No. What to do throw an Exception
# What happens if array is empty
# What happens if array is None
# Are we guranteed all three numbers will appear?

#Edge Cases: [], None, [4]
#Base Cases: [1], [0,1], 
#Regular case: [2,1,0], [2,2,0], [1,1,1]

#low_boundary = 1
#high_boundary = 1
#pivot = 1

# [0,0,1,1,1,1,2,2], pivot = 1

def red_white_blue_flag(lst):
    if lst == None or len(lst) ==0:
        return lst

    flag = [0,1,2]
    indx = 0
    low = 0
    high = len(lst) -1
    pivot = 1

    while indx <= high:
        num = lst[indx]
        if num not in flag:
            raise ValueError('Number not in flag')
        elif num < pivot:
            swap(indx, low, lst)
            low +=1
            indx += 1
        elif num > pivot:
            swap(indx, high, lst)
            high -= 1
        else:
            indx += 1 
    return lst

# print(red_white_blue_flag([1,0,1,2,1,0,1,2]))
# print(red_white_blue_flag([]))
# print(red_white_blue_flag(None))
# print(red_white_blue_flag([4]))
# print(red_white_blue_flag([1]))
# print(red_white_blue_flag([0,1]))
# print(red_white_blue_flag([1,1,1]))
# print(red_white_blue_flag([2,2,0]))
# print(red_white_blue_flag([2,1,0]))



#Edge Cases: [], None, [4]
#Base Cases: [1], [0,1], 
#Regular case: [2,1,0], [2,2,0], [1,1,1]