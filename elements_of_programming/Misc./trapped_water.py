# Write a function that calculates how many squares of rain would be captured 
# for a set of building heights. Weve given you a stub:



# Time: O(n**2)
# Space: O(1)
# def rain(heights):
#     """How much rain is trapped in between buildings"""
 
#     if len(heights) == 0:
#         return 0

#     count = 0
#     max_left = heights[0]
    
#     for indx in range(1,len(heights)-1):              
#         if max_left < heights[indx]:
#             max_left = heights[indx]
            

#         max_right = max(heights[indx+1:])
    
            
#         min_val = min(max_left, max_right)
#         diff = min_val - heights[indx]
#         if diff > 0:
#             count += diff
#     return count 


#Time: O(n)
#Space: O(n)
def rain(heights):

    right_building = [0] * len(heights)
    left_max = 0
    right_max = 0
    count = 0
    for indx in reversed(range(len(heights))):
        if heights[indx] > right_max:
            right_max = heights[indx]

        right_building[indx] = right_max

    for indx in range(len(heights)):              
        if left_max < heights[indx] or left_max == 0:
            left_max = heights[indx]
   
        
        min_val = min(left_max, right_building[indx])
        diff = min_val - heights[indx]
        # print diff
        if diff > 0:
            count += diff
    return count 





print rain([2,5,2,3,4])

