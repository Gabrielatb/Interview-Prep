# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #[-2*,1,-3,4,-1,2,1,-5*,4]
    #      [4,-1,2,1] has the largest sum = 6.
    
        
    curr_max, max_sum = nums[0], nums[0]
    
    for i in range(1, len(nums)):
        curr_max = max(nums[i], curr_max + nums[i])
        if curr_max > max_sum:
            max_sum = curr_max
            
    return max_sum