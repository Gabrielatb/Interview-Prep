# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.



def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
#Time Complexity O(n**2), Space Complexity O(1)

#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return i, j
# 

    # dict_ = {}
    # for i, num in enumerate(nums):
    #     if num not in dict_:
    #             dict_[num] = i
    #     elif num in dict_:
    #             dict_[num] = [dict_[num], i]
    # print dict_
 
    # for elem in nums:
    #     to_find = target - elem
    #     if to_find == elem and len(dict_[elem]) > 1:
    #         return dict_[elem]
    #     elif to_find in dict_:
    #         return dict_[elem], dict_[to_find]

    #time: O(n), space: O(n)
    dict_ = {}
    for i, nums in enumerate(nums):
        to_find = target - nums
        if nums in dict_:
            return dict_[nums], i
        dict_[to_find] = i
            
       


print twoSum([2,7,11,15], 9)
            
        