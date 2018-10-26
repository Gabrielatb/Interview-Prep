# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
from collections import OrderedDict 
import operator


# key: number
# value: count 
#time: O(nlogn)
#space: O(n)
def k_most_frequent(nums, k):

    d = OrderedDict()

    for num in nums:
        if num in d:
            d[num] +=1

        else:
            d[num] = 1

    sorted_dict = sorted(d.items(), key=operator.itemgetter(1))
    return_lst = []
    for item in sorted_dict[-k:]:
        return_lst.append(item[0])
    return return_lst


nums = [1,1,1,2,2,3]
k = 2
print k_most_frequent(nums, k)