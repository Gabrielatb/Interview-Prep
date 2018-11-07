# #merge sort implementation from my code school

# Runtime O(nlog(n))
# Space Complexity O(n)

def merge(nums, left, right):

    l_indx = 0
    r_indx = 0
    nums_indx = 0

    while len(left) > l_indx and len(right) > r_indx:
        if left[l_indx] < right[r_indx]:
            nums[nums_indx] = left[l_indx]
            l_indx += 1
        else:
            nums[nums_indx] = right[r_indx]
            r_indx += 1
        nums_indx += 1


    while len(left) > l_indx:
        nums[nums_indx] = left[l_indx]
        l_indx += 1
        nums_indx += 1

    while len(right) > r_indx:
        nums[nums_indx] = right[r_indx]
        r_indx += 1
        nums_indx += 1

    return nums





def merge_sort(lst):
    if len(lst) < 2:
        return lst

    mid = len(lst) / 2
    left = lst[:mid]
    right = lst[mid:]

    merge_sort(left)
    merge_sort(right)
    merge(lst, left, right)


    return lst
print merge_sort([5,4,9,2,1])




































