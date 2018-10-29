# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# from collections import OrderedDict 
# import operator


# key: number
# value: count 
#time: O(nlogn)
#space: O(n)
# def k_most_frequent(nums, k):

#     d = OrderedDict()

#     for num in nums:
#         if num in d:
#             d[num] +=1

#         else:
#             d[num] = 1

#     sorted_dict = sorted(d.items(), key=operator.itemgetter(1))
#     return_lst = []
#     for item in sorted_dict[-k:]:
#         return_lst.append(item[0])
#     return return_lst


from heapq import heappush, heappop

#time O(klogd)
#O(d)

def k_most_frequent(nums, k):
    freq_nums_dict = {}

    for num in nums:
        print num
        freq_nums_dict[num] = freq_nums_dict.get(num, 0) + 1

    heap = []
    for key in freq_nums_dict:
        heappush(heap, (freq_nums_dict[key], key))

    while len(heap) > k:
        heappop(heap)

    result = []
    for elem in heap:
        result.append(elem[1])

    return result












nums = [1,1,1,2,2,3]
k = 2
print k_most_frequent(nums, k)