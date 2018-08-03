# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

       
        #linear time complexity 
    
        dict_nums = {}

        for num in nums:
            if num in dict_nums:
                dict_nums[num] += 1

            else:
                dict_nums[num] = 1

        print dict_nums
        for key in dict_nums:
            print key, dict_nums[key]
            if dict_nums[key] == 1:
                print "inside return statement"
                return key

        return None


        
            