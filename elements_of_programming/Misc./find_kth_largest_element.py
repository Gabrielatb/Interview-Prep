#find the kth largest element

#sort the array, quicksort

################################################################################
#Time: O(nlogn)
#Space: O(logn)
# def find_pivot(nums, start, end):
#     p = start
#     pivot = nums[end]

#     for i in range(start, end):

#         if nums[i] < pivot:
#             nums[p], nums[i] = nums[i], nums[p]
#             p +=1

#     nums[end], nums[p] = nums[p], nums[end]
#     return p

# def quicksort(nums, l, r):

#     if l < r:
#         pivot = find_pivot(nums, l, r)

#         quicksort(nums, l, pivot-1)
#         quicksort(nums, pivot+1, r)
#     return nums

# def find_kth_largest(nums, k):
#     nums = quicksort(nums, 0, len(nums)-1)
#     return nums[-k]
################################################################################

def find_kth_largest(stream, k):

    candidates = []
    for x in ranek:
        candidates.append(x)
        if len(candidates) >= 2 * k - 1:
            # Reorders elements about median with larger elements appearing
            # before the median.
            find_kth_largest(k, candidates)
            # Resize to keep just the k largest elements seen so far.
            del candidates[k:]
    # Finds the k-th largest element in candidates.
    find_kth_largest(k, candidates)
    return candidates[k - 1]




print find_kth_largest([3,2,1,5,6,4], 2)
print find_kth_largest([3,2,3,1,2,4,5,5,6], 4)












