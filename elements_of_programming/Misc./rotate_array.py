#rotate an array by i 

# [1,2,3,4,5], rotate by 3
# output [3,4,5,1,2]


# Time: O(n)
# Space: O(n)
# def rotate_array(nums, k):
#     return_array = [0] * len(nums)

#     for i in range(len(nums)):
#         indx = (i + k) % len(nums)

#         return_array[indx] = nums[i]
#     return return_array




# Time: O(n*k)
# Space: O(1)
# def rotate_array(nums, k):

#     while k > 0:
#         temp_prior = nums[0]
#         temp = nums[0]
#         for indx in range(len(nums)-1):
#             temp = temp_prior
#             temp_prior = nums[indx+1]
#             print 'this is temp prior'
#             nums[indx+1] = temp
#             print indx, nums
            
            
      
#         nums[0] = temp_prior
#         print nums
#         k -=1

#     return nums

#Time: O(N)
#Space: O(1)
# def rotate_array(nums, k):

#     start = 0
#     count = len(nums)
#     while count > 0:
#         pre = nums[start]
#         n = start
#         while True:
#             n = (n + k) % len(nums)
#             tmp = nums[n]
#             nums[n] = pre
#             pre = tmp
#             count -= 1
#             print nums
#             if n == start:
#                 break
#         start += 1
      

#     return nums
# Time: O(n)
# Space: O(1)
def rotate_array(nums, k):
    k = k % len(nums)
    def reverse(beg, end, nums):
        while beg < end:
            nums[beg], nums[end] = nums[end], nums[beg]
            beg += 1
            end -=1

    reverse(0, len(nums)-1, nums)
    reverse(0, k-1, nums)
    reverse(k, len(nums)-1, nums)
    return nums






# [5,6,1,2,3,4]
nums = [1,2,3,4,5,6]
k=2
# nums = [1, 2, 3, 4, 5]
# k = 3
print rotate_array(nums, k)



