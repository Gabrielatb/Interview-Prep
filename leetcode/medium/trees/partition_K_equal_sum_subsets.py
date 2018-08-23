# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

# Example 1:
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# Note:

# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.

def canPartitionKSubsets(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
        
    #first find out target sum
    sums = [0]*k
    subsum = sum(nums) / k
    nums.sort(reverse=True)
    l = len(nums)
    
    def walk(i):
        if i == l:
            return len(set(sums)) == 1
        for j in xrange(k):
            sums[j] += nums[i]
            if sums[j] <= subsum and walk(i+1):
                return True
            sums[j] -= nums[i]
            if sums[j] == 0:
                break
        return False        
    
    return walk(0)


print canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)

#in our case we know that there are 4 subsets and there sum should be 5