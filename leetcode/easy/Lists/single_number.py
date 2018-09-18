# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4

def one_elem(lst):


    #Time Complexity: O(n**2)
    #Space Complexity: O(n)
    return_lst = []
    for num in nums:
        if num not in return_lst:
            return_lst.append(num)
        else:
            return_lst.remove(num)
    return return_lst.pop()



# print one_elem([2,2,1])
# print one_elem([4,1,2,1,2])
# print one_elem([17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6])

    #Runtime O(n)
    #Space Complexity O(n)
    dict_ = {}
    
    for num in nums:
        if num not in dict_:
            dict_[num] = 1
        else:
            dict_[num] += 1
            
    for key in dict_:
        if dict_[key] == 1:
            return key


    #Runtime: O(n)
    #Space Complexity: O(n)
    return (2 * sum(set(nums))) - sum(nums)

















        
#             