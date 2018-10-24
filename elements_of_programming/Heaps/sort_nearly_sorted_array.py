# Sort a nearly sorted (or K sorted) array
# Given an array of n elements, where each element is at most k away from its target position,
# devise an algorithm that sorts in O(n log k) time. For example, let us consider k is 2, 
# an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

# Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
#             k = 3 
# Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

# Input : arr[] = {10, 9, 8, 7, 4, 70, 60, 50}
#          k = 4
# Output : arr[] = {4, 7, 8, 9, 10, 50, 60, 70}

#this can be more efficiently sorted with a heap data structure taking into advantage
#the fact that the array is almost sorted

import heapq
import itertools
def almost_sorted_array(sequence, k):

    min_heap = []
    # Adds the first k elements into min_heap. Stop if there are fewer than k
    # elements.
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    result = []
    # For every new element, add it to min_heap and extract the smallest.
    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    # sequence is exhausted, iteratively extracts the remaining elements.
    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result


# def almost_sorted_array(array, k):
#     min_heap = []
#     #adding first k elements into min_heap
#     for x in itertools.islice(array, k):
#         heapq.heappush(min_heap, x)

#     result = []
#     #new elements add to min heap and extract the smallest
#     for num in array:
#         smallest = heapq.heappushpop(min_heap, num)
#         result.append(smallest)

#     while min_heap:
#         smallest = heapq.heappop(min_heap)
#         result.append(smallest)

#     return result


print almost_sorted_array([3,-1,2,6,4,5,8], 2)


#################################################################################


#quick sort 
# x
# def partition(lst, start, end):
#     p_index = start
#     pivot = lst[end]

#     for i in range(start, end):
#         if lst[i] < pivot:
#             lst[i], lst[p_index] =  lst[p_index], lst[i]
#             p_index +=1

#     lst[p_index], lst[end] = lst[end], lst[p_index]

#     return p_index


# def quicksort(lst, start, end, k):
#     k -=1

#     if start < end:

#         p_index = partition(lst, start, end)

#         quicksort(lst, start, p_index - 1, k)
#         quicksort(lst, p_index + 1, end, k)

#     return lst

# def quicksort_start(lst, k):
#     return quicksort(lst, 0, len(lst)-1, k)

# lst = [10, 9, 8, 7, 4, 70, 60, 50]
# print quicksort(lst, 0, len(lst)-1, 4)