# Video 1: (Level: Easy) Reverse the order of elements in an array. For example, A = [1,2,3,4,5,6], Output = [6,5,4,3,2,1]

# def swap(lst, start, end):
#     temp = lst[start]
#     lst[start] = lst[end]
#     lst[end] = temp

def reverse_array(lst):
    if lst == None or len(lst) == 0 or len(lst) == 1:
        return lst
    start=0
    end=len(lst) - 1
    while start < end:
        swap(lst, start, end)
        start +=1
        end -=1
    return lst

#time -> O(n)
#space -> O(1)
# print(reverse_array([1,2,3,4,5,6]))
# print(reverse_array([]))
# print(reverse_array(None))
# print(reverse_array([1]))
# print(reverse_array([1,2]))

# Level: Easy2 Sum Problem: Given a sorted array of integers, find two numbers in the array that sumto a given integer target.For example, if a = [1,2,3,5,6,7] and target = 11, the answer will be 5 and 6.

def find_two_sum(lst, target):
    if lst == None or len(lst) == 0:
        return None

    start = 0
    end = len(lst) -1 
    while start < end:
        sum_of_two = lst[start] + lst[end]
        if sum_of_two == target:
            return lst[start], lst[end]
        elif sum_of_two > target:
            end -= 1
        else:
            start += 1
    return None

# time: O(N)
# space: O(1)

# print(find_two_sum([1,2,3,5,6,7], 11))
# print(find_two_sum([], 0))
# print(find_two_sum(None, 0))
# print(find_two_sum([1,2,3,5,6,7], 100))
# print(find_two_sum([1,2,3,5,6,7], 0))

# Given a sorted array in non-decreasing order, return an array of squares of each number, also in non-decreasing order. For example:

# [-4,-2,-1,0,3,25] -> [0,1,4,9,16,25]

# How can you do it in O(n) time?


#start = 0
#end -1


def square_array(lst):
    new_array = []
    start = 0
    end = len(lst) -1
    while start < end:
        start_squared = lst[start] ** 2 
        end_squared = lst[end] ** 2 
        if abs(lst[start]) > abs(lst[end]):
            new_array.insert(0, start_squared)
            start +=1 
        else:
            new_array.insert(0, end_squared)
            end -=1
    return new_array

# print(square_array([-4,-2,-1,0,3,5]))
# [16, 4, 1, 0, 9, 25]
# 
# [-4,-2,-1,0,3,25]

#[-4, 0, 1, 2, 3]

# Given an array of integers, find the continuous subarray, which when sorted, results in the entire array being sorted. For example: A = [0,2,3,1,8,6,9], result is the subarray [2,3,1,8,6]

#start -> -2
#end ->  1
#Are we guranteed it's only numbers
#what should we do if it's empty array, return null
#what should we do if it's null value is given, return null
#what to return if the array is already sorted, return null


# [0,2,3,1,8,6,9] --> [2,3,1,8,6]
# [1,2,4,5,3,5,6,7] --> [4,5,3]
# [1,3,5,2,6,4,7,8,9] --> [3,5,2,6,4]


#iterate forward if no dips, return null else save dip index
#iterate backwards, find spike, save spike index

#find min value, search left to include all values greater than min

#find max value, search right to include all values less than max

#Test Cases
# edge cases => empty array, null value
#base case => one element, 2 elements (sorted and unsorted)
#regular case => array already sorted, unsorted portion is beginning, vs. end

def return_continuous_subarray(lst):
    if lst == None or len(lst) == 0:
        return None

    start = None
    for indx in range(len(lst) -1):
        if lst[indx + 1] < lst[indx]:
            start = indx
            break;

    #list has been sorted
    if start == None:
        return None

    end = None
    for indx in range(len(lst) -1, 0, -1):
        if lst[indx -1] > lst[indx]:
            end = indx
            break;

    #find min and max value
    max_value = float('-inf')
    min_value = float('inf')
    for indx in range(start, end + 1):
        if lst[indx] > max_value:
            max_value = lst[indx]

        if lst[indx] < min_value:
            min_value = lst[indx]

    for indx in range(0, start):
        if lst[indx] > min_value:
            start = indx

    for indx in range(end, len(lst) -1):
        print(lst)
        print(lst[indx])
        if lst[indx] < max_value:
            end = indx

    return start, end

# Time Complexity: O(n)
# Space Complexity: O(1)
# print(return_continuous_subarray([0,2,3,1,8,6,9]))
# print(return_continuous_subarray([1,2,4,5,3,5,6,7]))
# print(return_continuous_subarray([1,3,5,2,6,4,7,8,9]))
# print(return_continuous_subarray([2,1]))



# [1,2,4,5,3,5,6,7] --> [4,5,3] - If you sort from indices 2 to 4, the entire array is sorted.[1,3,5,2,6,4,7,8,9] --> [3,5,2,6,4] -  If you sort from indices 1 to 5, the entire array is sorted.