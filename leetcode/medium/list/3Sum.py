# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
#Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        length, result = len(nums), []

        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i] * -1
            s, e = i+1, length-1
            while s < e:
                if nums[s] + nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s +=1
                    while s < e and nums[s] == nums[s-1]:
                        s+=1

                elif nums[s] + nums[e] < target:
                    s +=1
                else:
                    e -=1
        return result
