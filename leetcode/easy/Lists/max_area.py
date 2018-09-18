# Given n non-negative integers a1, a2, ..., an , where each represents a point at
# coordinate (i, ai). n vertical lines are drawn such that the two endpoints of 
#line i is at (i, ai) and (i, 0). 
#Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

 



# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

# Example:

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49







class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # max_value = 0
        # l = 0
        # r = len(height) - 1

        # while l < r:
        #     h = min(height[l], height[r])
        #     width = r - l
        #     area = h * width
        #     if area > max_value:
        #         max_value = area
        #     if height[l] < height[r]:
        #         l = l+1
        #     else:
        #         r = r-1

        # return max_value
        
        
        
        # max_area = 0
        
        # for i in range(len(height)-1):
        #     for j in range(i+1, len(height)):
        #         area = min(height[i], height[j]) * abs(j-i)
        #         if area > max_area:
        #             max_area = area
                    
        # return max_area
                




        max_area = 0
        
        #two pointers 
        lo, hi = 0, len(height) -1 
        
        while lo < hi:
            diff = hi-lo
            min_val = min(height[lo], height[hi])
            area = diff * min_val
            if area > max_area:
                max_area = area
            else:
                if height[lo] > height[hi]:
                    hi -=1
                else:
                    lo +=1
        return max_area
