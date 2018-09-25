# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

# Example 1:
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: 
#It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        target = sum(nums) /k
        
        if isinstance(target, float) == True:
            return False
        if len(nums) < k:
            return False
        def partition(groups):
            if not nums:
                return True
            val = nums.pop()
            
            for i, group in enumerate(groups):
                if group + val <= target:
                    groups[i] += val
                    if partition(groups):
                        return True
                    else:
                        groups[i] -=val
                if group == 0:
                    break
                    
            nums.append(val)
            return False
        
        nums.sort()
        if nums and nums[-1] == target:
            nums.pop()
            k -=1
            
        groups = [0] * k
        return partition(groups)
