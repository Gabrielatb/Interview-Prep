#generic quicksort implementation


# def quicksort(lst):

#     if len(lst) <= 1:
#         return lst

#     lo, eq, hi = [], [], []

#     pivot = len(lst)/2

#     for num in lst:
#         if num < lst[pivot]:
#             lo.append(num)
#         elif num > lst[pivot]:
#             hi.append(num)
#         else:
#             eq.append(num)

#     return quicksort(lo) + eq + quicksort(hi)



# print quicksort([4,7,3,9,0,22,])


#Runtime O(nlogn) average, worst case O(n**2)
#space: O(logn)
# After partitioning, the partition with the fewest
# elements is (recursively)
# sorted first, requiring at most O(log n) space. 
def find_pivot(nums, start, end):
    p_indx = start
    pivot = nums[end]

    for indx in range(start, end):
        if nums[indx] < pivot:
            nums[indx], nums[p_indx] = nums[p_indx], nums[indx] 
            p_indx += 1

    nums[p_indx], nums[end] = nums[end], nums[p_indx]
    return p_indx

def quicksort(nums, lo, hi):
    if lo < hi:
        pivot = find_pivot(nums, lo, hi)

        quicksort(nums, pivot+1, hi)

        quicksort(nums, lo,  pivot-1)

    return nums


nums = [4,7,3,9,0,22,]
print quicksort(nums, 0, len(nums)-1)