#problem also found on leetcode


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
    
        if not nums:
            return -1
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
        
            mid = (high + low ) /2
            
            if nums[mid] == target:
                return mid

            elif nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
                    
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid +1
                else:
                    high = mid -1

        return -1 