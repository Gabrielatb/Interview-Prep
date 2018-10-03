# Given a sorted array nums, remove the duplicates in-place 
# such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying 
# the input array in-place with O(1) extra memory.


# Given nums = [1,1,2],

# Your function should return length = 2


# Given nums = [0,0,1,1,1,2,2,3,3,4],

# Your function should return length = 5

#[0, 1*, 2, 3, 1, 2, 2, 3*, 3, 4 ]


# Time Complexity: O(n)
# Space Complexity: O(1)

def remove_dups(lst):

    if not lst: return 0

    indx = 0

    for i in range(1, len(lst)):
        if lst[i] != lst[indx]:
            lst[indx+1] = lst[i]
            indx += 1

    return indx + 1



    # if not lst:
    #     return 0
#     slow = 0
#     fast = 1
#     count = 1
#     while fast < len(lst):
#         if lst[slow] == lst[fast]:
#             fast += 1 
#         else:
#             lst[slow + 1] = lst[fast] 
#             count +=1
#             slow +=1
#     return count

print remove_dups([0,0,1,1,1,2,2,3,3,4])

    
